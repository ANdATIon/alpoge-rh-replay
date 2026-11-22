# P0177: M016753 port evidence

This is a partial port submission for [Port P0177, issue #32545](https://github.com/rohanarun/alpoge-rh-replay/issues/32545).
It adds one record, `port/patches/M016753.json`, with `"notes": "unchanged"`.
No source patch is needed. The theorem statement and proof are byte-identical to the pinned archive.

## Scope

| Module | Role | Result |
| --- | --- | --- |
| M016753: `COnePropertyFiniteExtension` | New P0177 target | Built unchanged |
| M044443: `NormCompHomogeneousIsHomogeneous` | Accepted transitive import | Built with its existing accepted coefficient-notation patch |
| M044444: `NormCompHomogeneousIsHomogeneousStatement` | Accepted direct import | Built unchanged |

All module names above are under `Development.AbelianVarietyTheory.Proofs.DivisorProofs`.
Only M016753 receives a new record. Existing import and packet records are preserved.

## Inputs and build

- Lean: `leanprover/lean4:v4.36.0`, compiler commit `611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9`.
- Mathlib: `fc4f59e577feb1a4956671bc04ac18aaaf8cd842` (`v4.36.0`).
- Selection/build base: `88e62d766df56e1be0150bb77ed3947268f1e564`.
- The published archive's 14 parts were verified against `parts.sha256`.
- Every target/import source was extracted from that archive and verified against `tracker/modules.jsonl.gz` before applying the accepted import patch.
- A fresh sparse project used the unmodified repository `scripts/port-ci-build.py` project-file generator, preserving the archive's applicable Lean options.
- Only exact target dependency packages were copied. The project had no `.lake/build` outputs before compilation.
- Each of the three project modules was compiled in dependency order using `lake --no-cache build +<Module>:olean` with `LEAN_NUM_THREADS=1`.

The [receipt](receipt.json) contains exact commands, source/patch/record/object/log digests, archive-part hashes, all dependency revisions, and the complete generated project configuration.
The [combined transcript](build.log) includes every fresh build. Individual logs are in [logs](logs).
Later target builds may replay an import that was freshly built earlier in this same run; each project module also has its own successful `Built` transcript.

Both unchanged upstream elaborated auditors ran over all three modules:

- [IsLattice audit](islattice-audit.log): exit 0, no findings.
- [Reused-name audit](reused-audit.log): exit 0, no findings.

Their exact script hashes and commands are recorded in the receipt. No `sorry`, `admit`, axioms, `native_decide`, `implemented_by`, or `unsafe` were added to any proof source.
The [repository validator](validation.log) passed.

## Packet remains incomplete

| Remaining unported module | Missing accepted project import |
| --- | --- |
| M006414 | M005069 |
| M006833 | M005055 |
| M016272 | M041462 |

The packet has 57 previously accepted members, this one submitted member, and the three blocked live members above.
Pruned IDs excluded from the packet are M015244, M015392, and M016703.
The [selection record](selection.json) lists all previously accepted IDs and the exact partial selection.
No queued dependency PR was treated as an accepted import.

This evidence does not establish full packet completion, earn replay credit, or give a full-RH verdict. Replay pins and infrastructure are unchanged.
