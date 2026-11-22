# Independent replay of Alpöge’s RH release

Levent Alpöge announced a Lean proof of the Riemann Hypothesis on November 20, 2026. This repository records an independent attempt to check his published archive. Credit for the claimed proof belongs to Alpöge and his collaborators. [Original announcement](https://alpo.ge/remark.pdf)

## Current status

**Lean 4.36 port complete — now optimizing the Lean 4.36 proof.**

- **Porting & packet claims paused:** Please **do not** open new packet claims (`Claim P####` / `Claim M######`) or Lean 4.33.1 → 4.36.0 porting PRs. The full Lean `v4.36.0` port has landed upstream in [`leanprover-community/riemann-hypothesis`](https://github.com/leanprover-community/riemann-hypothesis) (`main`), and a consolidated 47,884-file build (`−67.9%` file count vs `main`) is staged in [PR #120](https://github.com/leanprover-community/riemann-hypothesis/pull/120) (`rohanarun/riemann-hypothesis` branch `opt/collapse-and-consolidate-4.36`).
- **New focus:** Simplifying, accelerating, and modularizing the Lean 4.36 proof while keeping `src/Challenge.lean`, `src/Statements.lean`, and `lake comparator` (`Lean paranoid` + `nanoda`) green.
- **Historical replay archive:** All volunteer credits, historical packet logs, and pinned 4.33.1 replay records remain preserved below and on the [live progress dashboard](https://rohanarun.github.io/alpoge-rh-replay/).

## Contributors

Thank you to all volunteers and agent contributors who helped replay and port the initial 175,187-module release! If you are running an agent or looking to contribute now, use the **Lean 4.36 optimization prompt** below instead of claiming legacy packets.

<!-- volunteer-roster-start -->

**Replay volunteers (104)**

[@123454321bobbob-tech](https://github.com/123454321bobbob-tech), [@1337isnot1337](https://github.com/1337isnot1337), [@21Z121Z1](https://github.com/21Z121Z1), [@aapolipponen](https://github.com/aapolipponen), [@agi-for-my-llama](https://github.com/agi-for-my-llama), [@Amahane-Hikari](https://github.com/Amahane-Hikari), [@amrehan](https://github.com/amrehan), [@ANdATIon](https://github.com/ANdATIon), [@angusbarry](https://github.com/angusbarry), [@arxhr007](https://github.com/arxhr007), [@aulafy](https://github.com/aulafy), [@BenCaunt](https://github.com/BenCaunt), [@BouquetAntoine](https://github.com/BouquetAntoine), [@Brendon-Hablutzel](https://github.com/Brendon-Hablutzel), [@burbon](https://github.com/burbon), [@certified-retart](https://github.com/certified-retart), [@ChristosMaglaras](https://github.com/ChristosMaglaras), [@chriswilson413](https://github.com/chriswilson413), [@CubeJerry](https://github.com/CubeJerry), [@DanieleCorso](https://github.com/DanieleCorso), [@dga471](https://github.com/dga471), [@dgahelper](https://github.com/dgahelper), [@dh5at](https://github.com/dh5at), [@dhudakk](https://github.com/dhudakk), [@drew2apps](https://github.com/drew2apps), [@EF-Code](https://github.com/EF-Code), [@egergerfg](https://github.com/egergerfg), [@emsi](https://github.com/emsi), [@Ethan-prog-netizen](https://github.com/Ethan-prog-netizen), [@f10etclawdbot](https://github.com/f10etclawdbot), [@florianmodel](https://github.com/florianmodel), [@gabeldev](https://github.com/gabeldev), [@galakurpi](https://github.com/galakurpi), [@Genius-Cai-wen-zheng](https://github.com/Genius-Cai-wen-zheng), [@gilad12-coder](https://github.com/gilad12-coder), [@gniax](https://github.com/gniax), [@HaqtanEfe](https://github.com/HaqtanEfe), [@hipotures](https://github.com/hipotures), [@HITEYY](https://github.com/HITEYY), [@iAndyHD3](https://github.com/iAndyHD3), [@IlluminPhoenix](https://github.com/IlluminPhoenix), [@JamCh01](https://github.com/JamCh01), [@JanSimeonMetzger](https://github.com/JanSimeonMetzger), [@jaykobdetar](https://github.com/jaykobdetar), [@jdenwood](https://github.com/jdenwood), [@jjjhenriksen](https://github.com/jjjhenriksen), [@jsnider3](https://github.com/jsnider3), [@juanfers1](https://github.com/juanfers1), [@jwr404](https://github.com/jwr404), [@krisyotam](https://github.com/krisyotam), [@LakshyAAAgrawal](https://github.com/LakshyAAAgrawal), [@ljagiello](https://github.com/ljagiello), [@loremcdmx](https://github.com/loremcdmx), [@Lv-00-ANI](https://github.com/Lv-00-ANI), [@m4tthewdavis](https://github.com/m4tthewdavis), [@mabdelazim](https://github.com/mabdelazim), [@maddoxjack](https://github.com/maddoxjack), [@matan1905](https://github.com/matan1905), [@matiasm15](https://github.com/matiasm15), [@maugomez77](https://github.com/maugomez77), [@maxime-fleury](https://github.com/maxime-fleury), [@mdpmcc](https://github.com/mdpmcc), [@Mfweb](https://github.com/Mfweb), [@misuadn-laplace](https://github.com/misuadn-laplace), [@MLEARNER701](https://github.com/MLEARNER701), [@MLTQ](https://github.com/MLTQ), [@mu-mei](https://github.com/mu-mei), [@Mzzj114](https://github.com/Mzzj114), [@nicu-chiciuc](https://github.com/nicu-chiciuc), [@Paulee314](https://github.com/Paulee314), [@pCwOrM](https://github.com/pCwOrM), [@rahulsundar477-star](https://github.com/rahulsundar477-star), [@rayy3535](https://github.com/rayy3535), [@RhizoNymph](https://github.com/RhizoNymph), [@rishabh-16](https://github.com/rishabh-16), [@RobertBarnettProjects](https://github.com/RobertBarnettProjects), [@sat3n](https://github.com/sat3n), [@Scratch-net](https://github.com/Scratch-net), [@SeriousRising](https://github.com/SeriousRising), [@Sethumathavanpk](https://github.com/Sethumathavanpk), [@shardmods](https://github.com/shardmods), [@Sigomi](https://github.com/Sigomi), [@sp20262026](https://github.com/sp20262026), [@surfyhou](https://github.com/surfyhou), [@t-choudhury](https://github.com/t-choudhury), [@ThatOneShortGuy](https://github.com/ThatOneShortGuy), [@TimShakespeare](https://github.com/TimShakespeare), [@TomMoeras](https://github.com/TomMoeras), [@TOTOGT](https://github.com/TOTOGT), [@Trefoiler](https://github.com/Trefoiler), [@TVSuchty](https://github.com/TVSuchty), [@twaldin](https://github.com/twaldin), [@unhingedpanda](https://github.com/unhingedpanda), [@UnityChaos](https://github.com/UnityChaos), [@user42245](https://github.com/user42245), [@varo6](https://github.com/varo6), [@vivekshivarajkumar](https://github.com/vivekshivarajkumar), [@walkingsophie](https://github.com/walkingsophie), [@whitegrave1917-web](https://github.com/whitegrave1917-web), [@WilmervH](https://github.com/WilmervH), [@WorldianAI](https://github.com/WorldianAI), [@Wronskode](https://github.com/Wronskode), [@yingluom](https://github.com/yingluom), [@zediir](https://github.com/zediir)

<!-- volunteer-roster-end -->

[Code contributors](https://github.com/rohanarun/alpoge-rh-replay/graphs/contributors) · [Volunteer activity chart](ACTIVITY.md)

### Active claims awaiting evidence

[Browse open granted claims on GitHub](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aclaim-granted).

<details>
<summary>Show active claims awaiting evidence</summary>

<!-- active-volunteers-start -->

[44 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
| [@gilad12-coder](https://github.com/gilad12-coder) | [M131258](https://github.com/rohanarun/alpoge-rh-replay/issues/25970) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M051277](https://github.com/rohanarun/alpoge-rh-replay/issues/26977) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M079827](https://github.com/rohanarun/alpoge-rh-replay/issues/26978) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M080139](https://github.com/rohanarun/alpoge-rh-replay/issues/26979) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M134025](https://github.com/rohanarun/alpoge-rh-replay/issues/26980) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M141042](https://github.com/rohanarun/alpoge-rh-replay/issues/26981) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M147088](https://github.com/rohanarun/alpoge-rh-replay/issues/26992) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M004289](https://github.com/rohanarun/alpoge-rh-replay/issues/26993) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M034703](https://github.com/rohanarun/alpoge-rh-replay/issues/26994) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M036491](https://github.com/rohanarun/alpoge-rh-replay/issues/27042) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M079838](https://github.com/rohanarun/alpoge-rh-replay/issues/27043) | Claimed |
| [@loremcdmx](https://github.com/loremcdmx) | [M140261](https://github.com/rohanarun/alpoge-rh-replay/issues/27044) | Claimed |
| [@maugomez77](https://github.com/maugomez77) | [M118430](https://github.com/rohanarun/alpoge-rh-replay/issues/27317) | Claimed |
| [@maugomez77](https://github.com/maugomez77) | [M116378](https://github.com/rohanarun/alpoge-rh-replay/issues/28207) | Claimed |
| [@maugomez77](https://github.com/maugomez77) | [M111760](https://github.com/rohanarun/alpoge-rh-replay/issues/28316) | Claimed |
| [@maugomez77](https://github.com/maugomez77) | [M113163](https://github.com/rohanarun/alpoge-rh-replay/issues/28725) | Claimed |
| [@user42245](https://github.com/user42245) | [M164325](https://github.com/rohanarun/alpoge-rh-replay/issues/28949) | Claimed |
| [@user42245](https://github.com/user42245) | [M163709](https://github.com/rohanarun/alpoge-rh-replay/issues/28973) | Claimed |
| [@user42245](https://github.com/user42245) | [M168805](https://github.com/rohanarun/alpoge-rh-replay/issues/28987) | Claimed |
| [@UnityChaos](https://github.com/UnityChaos) | [P2771](https://github.com/rohanarun/alpoge-rh-replay/issues/30424) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[8,000 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@JamCh01](https://github.com/JamCh01) | [M078790](https://github.com/rohanarun/alpoge-rh-replay/issues/34918#issuecomment-7083573449) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083048](https://github.com/rohanarun/alpoge-rh-replay/issues/34919#issuecomment-7083592803) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083258](https://github.com/rohanarun/alpoge-rh-replay/issues/34920#issuecomment-7083581636) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083274](https://github.com/rohanarun/alpoge-rh-replay/issues/34921#issuecomment-7083586554) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083362](https://github.com/rohanarun/alpoge-rh-replay/issues/34922#issuecomment-7083579960) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083381](https://github.com/rohanarun/alpoge-rh-replay/issues/34923#issuecomment-7083584895) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083408](https://github.com/rohanarun/alpoge-rh-replay/issues/34924#issuecomment-7083587962) | Pending review |
| [@hipotures](https://github.com/hipotures) | [M058744](https://github.com/rohanarun/alpoge-rh-replay/issues/34925#issuecomment-7083549454) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083634](https://github.com/rohanarun/alpoge-rh-replay/issues/34926#issuecomment-7083589592) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083875](https://github.com/rohanarun/alpoge-rh-replay/issues/34927#issuecomment-7083591303) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083919](https://github.com/rohanarun/alpoge-rh-replay/issues/34928#issuecomment-7083583257) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M071348](https://github.com/rohanarun/alpoge-rh-replay/issues/34929#issuecomment-7083547475) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M071497](https://github.com/rohanarun/alpoge-rh-replay/issues/34930#issuecomment-7083538350) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M083941](https://github.com/rohanarun/alpoge-rh-replay/issues/34931#issuecomment-7083625852) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M084009](https://github.com/rohanarun/alpoge-rh-replay/issues/34932#issuecomment-7083621039) | Pending review |
| [@hipotures](https://github.com/hipotures) | [M061277](https://github.com/rohanarun/alpoge-rh-replay/issues/34933#issuecomment-7083563346) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M084022](https://github.com/rohanarun/alpoge-rh-replay/issues/34934#issuecomment-7083623670) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M084049](https://github.com/rohanarun/alpoge-rh-replay/issues/34935#issuecomment-7083640372) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M084086](https://github.com/rohanarun/alpoge-rh-replay/issues/34936#issuecomment-7083641976) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M084145](https://github.com/rohanarun/alpoge-rh-replay/issues/34937#issuecomment-7083633758) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[15,254 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@hipotures](https://github.com/hipotures) | [P2823](https://github.com/rohanarun/alpoge-rh-replay/issues/32509#issuecomment-7079303608) | 5 | [Build evidence verified](evidence/volunteers/P2823.json) |
| [@hipotures](https://github.com/hipotures) | [P2118](https://github.com/rohanarun/alpoge-rh-replay/issues/32372#issuecomment-7079123483) | 64 | [Build evidence verified](evidence/volunteers/P2118.json) |
| [@JamCh01](https://github.com/JamCh01) | [P2851](https://github.com/rohanarun/alpoge-rh-replay/issues/32233#issuecomment-7079805584) | 1 | [Build evidence verified](evidence/volunteers/P2851.json) |
| [@JamCh01](https://github.com/JamCh01) | [P2822](https://github.com/rohanarun/alpoge-rh-replay/issues/32210#issuecomment-7079026106) | 4 | [Build evidence verified](evidence/volunteers/P2822.json) |
| [@hipotures](https://github.com/hipotures) | [P2826](https://github.com/rohanarun/alpoge-rh-replay/issues/32697#issuecomment-7079661981) | 3 | [Build evidence verified](evidence/volunteers/P2826.json) |
| [@hipotures](https://github.com/hipotures) | [P2104](https://github.com/rohanarun/alpoge-rh-replay/issues/32172#issuecomment-7078938326) | 64 | [Build evidence verified](evidence/volunteers/P2104.json) |
| [@JamCh01](https://github.com/JamCh01) | [P2821](https://github.com/rohanarun/alpoge-rh-replay/issues/32171#issuecomment-7078933112) | 4 | [Build evidence verified](evidence/volunteers/P2821.json) |
| [@hipotures](https://github.com/hipotures) | [P2131](https://github.com/rohanarun/alpoge-rh-replay/issues/32096#issuecomment-7078666147) | 64 | [Build evidence verified](evidence/volunteers/P2131.json) |
| [@JamCh01](https://github.com/JamCh01) | [P2820](https://github.com/rohanarun/alpoge-rh-replay/issues/32002#issuecomment-7078658972) | 6 | [Build evidence verified](evidence/volunteers/P2820.json) |
| [@hipotures](https://github.com/hipotures) | [P1797](https://github.com/rohanarun/alpoge-rh-replay/issues/32044#issuecomment-7078497976) | 64 | [Build evidence verified](evidence/volunteers/P1797.json) |
| [@hipotures](https://github.com/hipotures) | [P1829](https://github.com/rohanarun/alpoge-rh-replay/issues/32080#issuecomment-7078580345) | 64 | [Build evidence verified](evidence/volunteers/P1829.json) |
| [@JamCh01](https://github.com/JamCh01) | [P2816](https://github.com/rohanarun/alpoge-rh-replay/issues/31759#issuecomment-7078756681) | 6 | [Build evidence verified](evidence/volunteers/P2816.json) |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M104720](https://github.com/rohanarun/alpoge-rh-replay/issues/34759#issuecomment-7083141507) | 1 | [Build evidence verified](evidence/volunteers/M104720.json) |
| [@emsi](https://github.com/emsi) | [M067676](https://github.com/rohanarun/alpoge-rh-replay/issues/34757#issuecomment-7083225293) | 1 | [Build evidence verified](evidence/volunteers/M067676.json) |
| [@JamCh01](https://github.com/JamCh01) | [M042507](https://github.com/rohanarun/alpoge-rh-replay/issues/34756#issuecomment-7083203610) | 1 | [Build evidence verified](evidence/volunteers/M042507.json) |
| [@JamCh01](https://github.com/JamCh01) | [M037921](https://github.com/rohanarun/alpoge-rh-replay/issues/34753#issuecomment-7083211648) | 1 | [Build evidence verified](evidence/volunteers/M037921.json) |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M123501](https://github.com/rohanarun/alpoge-rh-replay/issues/34752#issuecomment-7083139794) | 1 | [Build evidence verified](evidence/volunteers/M123501.json) |
| [@JamCh01](https://github.com/JamCh01) | [M034792](https://github.com/rohanarun/alpoge-rh-replay/issues/34749#issuecomment-7083201969) | 1 | [Build evidence verified](evidence/volunteers/M034792.json) |
| [@JamCh01](https://github.com/JamCh01) | [M032791](https://github.com/rohanarun/alpoge-rh-replay/issues/34748#issuecomment-7083208342) | 1 | [Build evidence verified](evidence/volunteers/M032791.json) |
| [@BenCaunt](https://github.com/BenCaunt) | [M142750](https://github.com/rohanarun/alpoge-rh-replay/issues/34747#issuecomment-7083127369) | 1 | [Build evidence verified](evidence/volunteers/M142750.json) |

<!-- volunteers-end -->

</details>

## Completed parts

<!-- completed-start -->

| Evidence for distinct module IDs | Count |
|---|---:|
| Successful source build observed | 26,591 |
| Pilot proof object reused | 150 |
| Pilot downstream module kernel-checked | 1 |
| Distributed proof object reused | 16,970 |
| Volunteer build evidence reviewed | 65,657 |
| Worker target kernel replay reviewed | 72 |
| **Total with recorded module evidence** | **109,441 / 175,187** |

[See each completed part and its evidence](completed/README.md) · [Machine-readable ledger](tracker/completed.tsv)

<!-- completed-end -->

## Give this prompt to an agent

**Default: optimize the Lean 4.36 proof.**

> The Lean 4.36.0 port of the Riemann Hypothesis proof is complete—do NOT claim legacy packets or open Lean 4.33 -> 4.36 porting PRs in `rohanarun/alpoge-rh-replay`. Instead, help optimize, simplify, and speed up the Lean `v4.36.0` + Mathlib (`fc4f59e577feb1a4956671bc04ac18aaaf8cd842`) codebase in https://github.com/leanprover-community/riemann-hypothesis (and the consolidated 47,884-module branch `opt/collapse-and-consolidate-4.36` in https://github.com/rohanarun/riemann-hypothesis/pull/120).
>
> Focus on self-contained, verifiable improvements:
> 1. **Import & dependency pruning:** Remove unused transitive imports, flatten redundant pass-through wrapper files, and shorten import depth.
> 2. **Proof & tactic acceleration:** Speed up slow modules, replace heavy `simp`/`aesop`/`linarith` scripts with direct rewrites or lemmas, and eliminate `maxHeartbeats` bumps where possible.
> 3. **Mathlib deduplication:** Replace duplicated local helper definitions or lemmas with canonical Mathlib `v4.36.0` declarations.
>
> **Strict rules:** Never modify `src/Challenge.lean`, `src/Statements.lean`, or `comparator.json`. Never introduce `sorry`, `admit`, new `axiom`s, or unsafe features. Verify every touched module with `lake build <Target>` (and `lake build Main Challenge` + `lake comparator` for end-to-end PRs), and include before/after build times, import counts, and `.olean` sizes in your PR description.

[Optimization & agent notes](auto-research.md) · [Upstream Lean 4.36 repo](https://github.com/leanprover-community/riemann-hypothesis) · [Consolidated 4.36 PR #120](https://github.com/leanprover-community/riemann-hypothesis/pull/120) · [Historical replay archive](STATUS.md)

## Reproduce the check

On Linux, install the elan launcher and ensure its `lean` and `lake` commands are on your PATH. The script also requires Python 3.9 or later, Bash, Git, curl, GNU tar, sha256sum, a C toolchain, network access, and a large writable build volume. Run from this repository with a fresh output directory.

```bash
./verify.sh /path/to/empty/replay-directory
```

The script compares every archive part with its SHA-256 digest, checks the toolchain and mathlib revision, builds the final module from source, and writes the transcript to `replay.log` in the output directory. The pinned Lean compiler is 4.33.1 and the mathlib commit is `0df444a360eaa60ab8c11dca51a86af692955474`.

### Integrity checkpoints

The script checks for changes to its tools, records, and prepared dependency artifacts at stage boundaries. These checks are not an execution sandbox: they do not prevent concurrent or transient modifications by code running as the same user. In execution order:

1. **Archive verification.** Every downloaded archive part is checked against `parts.sha256` with `sha256sum -c`. The SHA-256 digests of `Audit.lean`, `parts.sha256`, and `audit/dependency-artifacts.py` are recorded before any archive code runs.
2. **Manifest pin.** Immediately after extraction — before elan installs the toolchain or Lake runs — the SHA-256 digest of the extracted `lake-manifest.json` is recorded.
3. **Toolchain integrity.** After `elan toolchain install`, immediately before a `--prepare-only` run returns, after the source build (immediately before the audit), and immediately before the fresh-kernel check: `bin/lean`, `bin/leanchecker` and `bin/lake`, and the shared libraries they load (`libleanshared.so`, `libLake_shared.so`, `libleanshared_1.so`, `libleanshared_2.so`, `libInit_shared.so`), still match the digests pinned in `verify.sh` from the official Lean 4.33.1 Linux release for the machine's architecture (x86_64 or AArch64), and `Audit.lean` and `parts.sha256` still match the digests recorded at step 1. Prints `REPLAY_INTEGRITY_CHECK_PASSED`.
4. **Dependency check.** After the Mathlib cache download (the mathlib checkout is separately pinned to the recorded commit above), immediately before a `--prepare-only` run returns, and again after the source build: `lake-manifest.json` still matches the digest recorded at step 2; every package the manifest records is a git checkout at the revision the manifest records, with no tracked file modified — a `git status` that itself fails is treated as a failure, not as a clean tree; the project tree's tracked files, if it is a git checkout, are likewise unmodified; and the packages directory contains no package the manifest does not record. Prints `REPLAY_DEPENDENCIES_PRISTINE_PASSED`.
5. **Prepared artifact baseline.** Before the project source build, `dependency-artifacts.json` records the prepared search path and hashes of dependency and standard-library `.olean`, `.olean.server`, `.olean.private`, `.ir`, `.ir.sig`, and `.so` files. The parent verifier retains the snapshot digest. Checks reject changes, removals, additions, redirected paths, and earlier search-path entries shadowing prepared modules. Generated setup inputs and traces are excluded. Final checks use the recorded search path without evaluating the project lakefile again; `Audit.lean` explicitly imports Mathlib before Main. Successful checks print `REPLAY_DEPENDENCY_ARTIFACTS_PASSED` before the final stages and again after each stage.

The artifact baseline establishes continuity from the prepared cache. It does not independently establish that the downloaded cache matches its source, and it does not cover project artifacts as dependencies. A clean Git checkout alone cannot establish cache identity: a valid alternate cached definition can pass both a statement check and fresh-kernel replay while the original dependency source remains untouched. The native regression in `tests/dependency-artifacts-native.py` demonstrates this distinction using a temporary toy dependency; it makes no claim about the RH archive.

## Read the evidence

1. `REPLAY_SOURCE_BUILD_PASSED` means Lake built the module containing the final theorem.
2. `REPLAY_AXIOM_AUDIT_PASSED` means the five public theorems in `Main` type-checked against their statements, which `Audit.lean` writes out with Mathlib definitions only. The audit rejects any reported axiom beyond propositional extensionality, classical choice, and quotient soundness.
3. `REPLAY_FRESH_KERNEL_PASSED` means Lean’s checker replayed the declarations imported by `Main` in a fresh environment. It uses the same Lean kernel implementation.

The integrity markers have separate scopes. `REPLAY_DEPENDENCIES_PRISTINE_PASSED` covers dependency Git revisions and tracked files. `REPLAY_INTEGRITY_CHECK_PASSED` covers the pinned toolchain binaries/shared libraries and the recorded audit/checker inputs. `REPLAY_DEPENDENCY_ARTIFACTS_PASSED` covers the prepared compiled dependency baseline and its import providers. None of these markers alone establishes the full proof result.

An optional statement check runs after these three when `REPLAY_STATEMENT_CHECK=1` is set. It compares the five theorems in `Main` with propositions elaborated in a module that imports only Mathlib, and prints `REPLAY_STATEMENT_CHECK_PASSED`. It can also be run against a completed checkout; see [audit/README.md](audit/README.md).

A completed report should include the exit status, all three outputs, the printed theorem and axioms, and a checksum for the archived transcript. A machine or storage failure leaves the mathematical claim unresolved.

## Optional determinant check

The [M115707 example](examples/M115707/README.md) compares a shorter local Gram determinant argument with the published module. This check runs separately from the volunteer replay.

## Volunteer activity

![Cumulative chart of volunteers, granted claims, and replay submissions](tracker/activity.svg)

[How the chart is counted](ACTIVITY.md) · [Event data](tracker/activity.tsv)

## License

The original replay tooling and documentation in this repository are available under the [MIT License](LICENSE). Upstream Lean source, Mathlib, and third-party artifacts retain their respective licenses.
