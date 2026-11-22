"""Integration tests for port claim selection on a miniature offline ledger."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import types
import unittest
from unittest.mock import Mock, patch


class PortClaimTests(unittest.TestCase):
    def setUp(self):
        self.issues = []
        self.modules = [
            dict(id=ident, packet=packet, module=f'Example.{ident}', depth=0, imports=[])
            for ident, packet in (
                ('M000001', 'P0001'), ('M000002', 'P0001'), ('M000003', 'P0002'),
            )
        ]
        tasks = types.SimpleNamespace(
            repo='owner/test', open_issues=lambda: iter(self.issues),
            module_rows=lambda: iter(self.modules),
        )
        path = Path(__file__).resolve().parents[1] / 'tracker' / 'port.py'
        spec = importlib.util.spec_from_file_location('port_under_test', path)
        self.port = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {'tasks': tasks}):
            spec.loader.exec_module(self.port)
        self.port.ported = set
        self.port.triage = dict
        self.gh = Mock()
        self.lookup = Mock()
        self.port.subprocess = types.SimpleNamespace(run=self.gh, check_output=self.lookup)
        self.main_records(None, None)

    def main_records(self, *records, lean=None):
        pins = json.loads((self.port.ROOT / 'port' / 'target.json').read_text())
        if lean is not None:
            pins['lean'] = lean
        result = {f'm{i}': entry for i, entry in enumerate(records)}
        result['pins'] = {'text': json.dumps(pins)}
        self.lookup.return_value = json.dumps({'data': {'repository': result}})

    def run_cli(self, *args):
        output = io.StringIO()
        with patch.object(sys, 'argv', ['port.py', *args]), contextlib.redirect_stdout(output):
            self.port.main()
        return output.getvalue()

    def reserve(self, target):
        self.issues.append({'title': f'Port {target}'})

    def test_next_skips_packet_with_reserved_member(self):
        self.reserve('M000001')
        self.assertEqual([line.split('\t')[0] for line in self.run_cli('next').splitlines()], ['P0002'])

    def test_claim_rejects_packet_with_reserved_member(self):
        self.reserve('M000002')
        with self.assertRaisesRegex(SystemExit, 'Port M000002'):
            self.run_cli('claim', 'P0001')
        self.gh.assert_not_called()

    def test_claim_rejects_member_of_reserved_packet(self):
        self.reserve('P0001')
        with self.assertRaisesRegex(SystemExit, 'Port P0001'):
            self.run_cli('claim', 'M000001')
        self.gh.assert_not_called()

    def test_claim_allows_independent_module(self):
        self.reserve('M000001')
        self.run_cli('claim', 'M000002')
        command = self.gh.call_args.args[0]
        self.assertEqual(command[:3], ['gh', 'issue', 'create'])
        self.assertEqual(command[command.index('--title') + 1], 'Port M000002')
        self.assertEqual(self.gh.call_args.kwargs, {'check': True})

    def test_completed_packet_or_module_is_rejected_even_with_empty_local_ledger(self):
        self.main_records({'oid': 'a'}, {'oid': 'b'})
        for target in ('P0001', 'M000002'):
            with self.subTest(target=target), self.assertRaisesRegex(SystemExit, 'already fully ported'):
                self.run_cli('claim', target)
            query = next(arg for arg in self.lookup.call_args.args[0] if arg.startswith('query='))
            self.assertIn('main:port/patches/M000002.json', query)
            self.assertEqual('main:port/patches/M000001.json' in query, target == 'P0001')
        self.gh.assert_not_called()

    def test_partly_ported_packet_can_still_be_claimed(self):
        self.main_records({'oid': 'a'}, None)
        self.run_cli('claim', 'P0001')
        self.gh.assert_called_once()

    def test_retarget_or_failed_lookup_cannot_open_issue(self):
        self.main_records(None, lean='different toolchain')
        with self.assertRaisesRegex(SystemExit, 'target changed'):
            self.run_cli('claim', 'M000002')
        self.lookup.side_effect = subprocess.CalledProcessError(1, 'gh')
        with self.assertRaises(subprocess.CalledProcessError):
            self.run_cli('claim', 'M000002')
        self.gh.assert_not_called()

    def test_show_accepts_a_single_module_id(self):
        self.assertEqual(self.run_cli('show', 'M000002').split(),
                         ['M000002', '0', 'untriaged', 'Example.M000002'])

    def test_multiple_claims_share_one_issue_scan(self):
        with patch.object(self.port.tasks, 'open_issues', return_value=iter([])) as scan:
            self.run_cli('claim', 'P0001', 'P0002')
        scan.assert_called_once()
        self.assertEqual(self.lookup.call_count, 2)
        self.assertEqual([call.args[0][call.args[0].index('--title') + 1]
                          for call in self.gh.call_args_list], ['Port P0001', 'Port P0002'])

    def test_pending_port_pr_reserves_packet_without_open_claim_issue(self):
        self.issues.append({'title': 'Port P0001 to Lean 4.36', 'pull_request': {}})
        self.assertEqual([line.split('\t')[0] for line in self.run_cli('next').splitlines()],
                         ['P0002'])
        for target in ['P0001', 'M000001']:
            with self.subTest(target=target), self.assertRaisesRegex(SystemExit, 'Port P0001'):
                self.run_cli('claim', target)
        self.gh.assert_not_called()

    def test_pending_module_port_pr_reserves_containing_packet(self):
        self.issues.append({'title': '[port] M000002: adapt coefficients', 'pull_request': {}})
        with self.assertRaisesRegex(SystemExit, 'Port M000002'):
            self.run_cli('claim', 'P0001')
        self.gh.assert_not_called()

    def test_pending_pr_recognition_accepts_case_labels_and_multiple_ids(self):
        self.issues.extend([
            {'title': 'Porting p0001 and M000003', 'pull_request': {}},
            {'title': 'M000002: compatibility fixes', 'pull_request': {},
             'labels': [{'name': 'port'}]},
        ])
        self.assertEqual(self.port.port_issues(), {'P0001', 'M000002', 'M000003'})

    def test_unrelated_prs_and_nonclaim_issues_do_not_reserve_ports(self):
        self.issues.extend([
            {'title': 'Replay P0001', 'pull_request': {}},
            {'title': 'Transport P0002', 'pull_request': {}},
            {'title': 'Question about Port P0001'},
            {'title': 'Port queue improvements', 'pull_request': {}},
        ])
        self.assertEqual(self.port.port_issues(), set())

    def test_later_pending_pr_conflict_prevents_entire_claim_batch(self):
        self.issues.append({'title': 'Port P0002', 'pull_request': {}})
        with self.assertRaisesRegex(SystemExit, 'Port P0002'):
            self.run_cli('claim', 'P0001', 'P0002')
        self.gh.assert_not_called()

    def test_later_reservation_conflict_prevents_all_creations(self):
        self.reserve('M000003')
        with self.assertRaisesRegex(SystemExit, 'Port M000003'):
            self.run_cli('claim', 'P0001', 'P0002')
        self.gh.assert_not_called()

    def test_invalid_or_overlapping_batch_prevents_all_creations(self):
        cases = [('P0001', 'P9999'), ('P0001', 'P0001'),
                 ('P0001', 'M000001'), ('M000001', 'P0001')]
        for targets in cases:
            with self.subTest(targets=targets), self.assertRaises(SystemExit):
                self.run_cli('claim', *targets)
        self.gh.assert_not_called()
        self.lookup.assert_not_called()

    def test_two_distinct_members_of_one_packet_do_not_overlap(self):
        self.run_cli('claim', 'M000001', 'M000002')
        self.assertEqual(self.gh.call_count, 2)

    def test_later_target_lookup_failure_prevents_all_creations(self):
        response = self.lookup.return_value
        self.lookup.side_effect = [response, subprocess.CalledProcessError(1, 'gh')]
        with self.assertRaises(subprocess.CalledProcessError):
            self.run_cli('claim', 'P0001', 'P0002')
        self.gh.assert_not_called()

    def test_later_completed_target_prevents_all_creations(self):
        available = self.lookup.return_value
        self.main_records({'oid': 'already-ported'})
        self.lookup.side_effect = [available, self.lookup.return_value]
        with self.assertRaisesRegex(SystemExit, 'P0002 is already fully ported'):
            self.run_cli('claim', 'P0001', 'P0002')
        self.gh.assert_not_called()

    def test_creation_failure_does_not_retry_or_hide_earlier_creation(self):
        self.gh.side_effect = [None, subprocess.CalledProcessError(1, 'gh')]
        with self.assertRaises(subprocess.CalledProcessError):
            self.run_cli('claim', 'P0001', 'P0002')
        self.assertEqual(self.gh.call_count, 2)

    def test_open_packet_claim_cap_blocks_excess_packet_claims_for_user(self):
        for i in range(100, 100 + self.port.MAX_OPEN_PACKET_CLAIMS):
            self.issues.append({'title': f'Port P0{i}', 'user': {'login': 'alice'}})
        with patch.object(self.port, 'current_github_login', return_value='alice'):
            with self.assertRaisesRegex(SystemExit, 'already holds'):
                self.run_cli('claim', 'P0001')
            self.gh.assert_not_called()
            # Single-module claims are still allowed
            self.run_cli('claim', 'M000001')
            self.assertEqual(self.gh.call_count, 1)

        with patch.object(self.port, 'current_github_login', return_value='bob'):
            self.run_cli('claim', 'P0002')
            self.assertEqual(self.gh.call_count, 2)


if __name__ == '__main__':
    unittest.main()
