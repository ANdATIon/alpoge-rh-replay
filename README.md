# Independent replay of Alpöge’s RH release

Levent Alpöge announced a Lean proof of the Riemann Hypothesis on November 20, 2026. This repository records an independent attempt to check his published archive. Credit for the claimed proof belongs to Alpöge and his collaborators. [Original announcement](https://alpo.ge/remark.pdf)

## Current status

**Full replay in progress.** No full RH verification receipt has been produced by this project. The [two-worker pilot](evidence/pilot-receipt.json) transferred 150 previously unbuilt modules; the primary reused them and kernel-checked one downstream module.

Current cloud progress is recorded in the [worker status report](STATUS.md). See the [live progress dashboard](https://rohanarun.github.io/alpoge-rh-replay/) for the module ledger breakdown.

## Contributors

Choose any of **175,187 module tasks** or one of **2,858 work packets**. Each module has a source digest, direct dependencies, import depth, and a coordinator snapshot state. Use the [contributor guide](CONTRIBUTING.md) to find an available packet, claim it, build it, and return evidence. Browse the [packet index](tracker/packets.tsv), [snapshot totals](tracker/summary.json), or [open volunteer claims](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue%20is%3Aopen%20in%3Atitle%20Claim).

Start with the [agent instructions](auto-research.md) to claim work and submit replay evidence. Start your evidence comment with `Replay submission` to be credited automatically. Maintainers review the evidence before marking a task complete.

Working on a new Lean proof? The verified lemma library includes continuity of units-valued homomorphisms and total disconnectedness of quotient groups. [Import and use the lemmas](examples/proof-reuse/README.md#use-the-lemmas)

If anyone has some large machines they would be happy to put CI runners on, please DM Kim Morrison here: [https://leanprover.zulipchat.com/#narrow/channel/113488-general/topic/Discussion.3A.20Alp.C3.B6ge.20Proves.20the.20Riemann.20Hypothesis/near/642446185](https://t.co/L6O32z700f)

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

[46 entries. View the full table](tracker/volunteer-tables/active/README.md).

| Contributor | Task | Status |
|---|---|---|
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
| [@BenCaunt](https://github.com/BenCaunt) | [M071904](https://github.com/rohanarun/alpoge-rh-replay/issues/34558) | Claimed |
| [@BenCaunt](https://github.com/BenCaunt) | [M142746](https://github.com/rohanarun/alpoge-rh-replay/issues/34562) | Claimed |

<!-- active-volunteers-end -->

</details>

<details>
<summary>Submitted for review</summary>

<!-- pending-volunteers-start -->

[7,772 entries. View the full table](tracker/volunteer-tables/pending/README.md).

| Contributor | Task | Review |
|---|---|---|
| [@JamCh01](https://github.com/JamCh01) | [M121353](https://github.com/rohanarun/alpoge-rh-replay/issues/34608#issuecomment-7082889527) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M121386](https://github.com/rohanarun/alpoge-rh-replay/issues/34609#issuecomment-7082893876) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M133709](https://github.com/rohanarun/alpoge-rh-replay/issues/34611#issuecomment-7082856943) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M066573](https://github.com/rohanarun/alpoge-rh-replay/issues/34612#issuecomment-7082847708) | Pending review |
| [@hipotures](https://github.com/hipotures) | [M167375](https://github.com/rohanarun/alpoge-rh-replay/issues/34613#issuecomment-7082883156) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M121474](https://github.com/rohanarun/alpoge-rh-replay/issues/34614#issuecomment-7082891146) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M121625](https://github.com/rohanarun/alpoge-rh-replay/issues/34615#issuecomment-7082915835) | Pending review |
| [@hipotures](https://github.com/hipotures) | [M167901](https://github.com/rohanarun/alpoge-rh-replay/issues/34616#issuecomment-7082897113) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M131643](https://github.com/rohanarun/alpoge-rh-replay/issues/34617#issuecomment-7082920838) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M131655](https://github.com/rohanarun/alpoge-rh-replay/issues/34618#issuecomment-7082930856) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M131686](https://github.com/rohanarun/alpoge-rh-replay/issues/34619#issuecomment-7082925882) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M131900](https://github.com/rohanarun/alpoge-rh-replay/issues/34620#issuecomment-7082935820) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M131904](https://github.com/rohanarun/alpoge-rh-replay/issues/34621#issuecomment-7082932522) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M132260](https://github.com/rohanarun/alpoge-rh-replay/issues/34622#issuecomment-7082924162) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M132262](https://github.com/rohanarun/alpoge-rh-replay/issues/34623#issuecomment-7082934089) | Pending review |
| [@hipotures](https://github.com/hipotures) | [M171658](https://github.com/rohanarun/alpoge-rh-replay/issues/34624#issuecomment-7082911387) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M132264](https://github.com/rohanarun/alpoge-rh-replay/issues/34625#issuecomment-7082927521) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M132266](https://github.com/rohanarun/alpoge-rh-replay/issues/34626#issuecomment-7082930276) | Pending review |
| [@gilad12-coder](https://github.com/gilad12-coder) | [M130720](https://github.com/rohanarun/alpoge-rh-replay/issues/34627#issuecomment-7082875533) | Pending review |
| [@JamCh01](https://github.com/JamCh01) | [M132276](https://github.com/rohanarun/alpoge-rh-replay/issues/34628#issuecomment-7082939038) | Pending review |

<!-- pending-volunteers-end -->

</details>

<details>
<summary>Reviewed builds</summary>

<!-- volunteers-start -->

[15,223 entries. View the full table](tracker/volunteer-tables/reviewed/README.md).

| Contributor | Task | Modules | Review |
|---|---|---:|---|
| [@sp20262026](https://github.com/sp20262026) | [M102621](https://github.com/rohanarun/alpoge-rh-replay/issues/21126#issuecomment-7062351852) | 1 | [Build evidence verified](evidence/volunteers/M102621.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102582](https://github.com/rohanarun/alpoge-rh-replay/issues/21175#issuecomment-7062403147) | 1 | [Build evidence verified](evidence/volunteers/M102582.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102589](https://github.com/rohanarun/alpoge-rh-replay/issues/21254#issuecomment-7062479752) | 1 | [Build evidence verified](evidence/volunteers/M102589.json) |
| [@sp20262026](https://github.com/sp20262026) | [M161237](https://github.com/rohanarun/alpoge-rh-replay/issues/21383#issuecomment-7062564472) | 1 | [Build evidence verified](evidence/volunteers/M161237.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102604](https://github.com/rohanarun/alpoge-rh-replay/issues/21544#issuecomment-7062614878) | 1 | [Build evidence verified](evidence/volunteers/M102604.json) |
| [@sp20262026](https://github.com/sp20262026) | [M161235](https://github.com/rohanarun/alpoge-rh-replay/issues/21614#issuecomment-7062701075) | 1 | [Build evidence verified](evidence/volunteers/M161235.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102583](https://github.com/rohanarun/alpoge-rh-replay/issues/21714#issuecomment-7062783894) | 1 | [Build evidence verified](evidence/volunteers/M102583.json) |
| [@sp20262026](https://github.com/sp20262026) | [M161240](https://github.com/rohanarun/alpoge-rh-replay/issues/21794#issuecomment-7062861368) | 1 | [Build evidence verified](evidence/volunteers/M161240.json) |
| [@maugomez77](https://github.com/maugomez77) | [M167105](https://github.com/rohanarun/alpoge-rh-replay/issues/21808#issuecomment-7068740380) | 1 | [Build evidence verified](evidence/volunteers/M167105.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102610](https://github.com/rohanarun/alpoge-rh-replay/issues/21912#issuecomment-7062974457) | 1 | [Build evidence verified](evidence/volunteers/M102610.json) |
| [@maugomez77](https://github.com/maugomez77) | [M155716](https://github.com/rohanarun/alpoge-rh-replay/issues/21922#issuecomment-7068850135) | 1 | [Build evidence verified](evidence/volunteers/M155716.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102609](https://github.com/rohanarun/alpoge-rh-replay/issues/22055#issuecomment-7063030992) | 1 | [Build evidence verified](evidence/volunteers/M102609.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102614](https://github.com/rohanarun/alpoge-rh-replay/issues/22085#issuecomment-7063077886) | 1 | [Build evidence verified](evidence/volunteers/M102614.json) |
| [@sp20262026](https://github.com/sp20262026) | [M062868](https://github.com/rohanarun/alpoge-rh-replay/issues/22108#issuecomment-7063132390) | 1 | [Build evidence verified](evidence/volunteers/M062868.json) |
| [@sp20262026](https://github.com/sp20262026) | [M062869](https://github.com/rohanarun/alpoge-rh-replay/issues/22166#issuecomment-7063225555) | 1 | [Build evidence verified](evidence/volunteers/M062869.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102593](https://github.com/rohanarun/alpoge-rh-replay/issues/22198#issuecomment-7063277327) | 1 | [Build evidence verified](evidence/volunteers/M102593.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102607](https://github.com/rohanarun/alpoge-rh-replay/issues/22219#issuecomment-7063334849) | 1 | [Build evidence verified](evidence/volunteers/M102607.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102617](https://github.com/rohanarun/alpoge-rh-replay/issues/22234#issuecomment-7063424448) | 1 | [Build evidence verified](evidence/volunteers/M102617.json) |
| [@sp20262026](https://github.com/sp20262026) | [M102625](https://github.com/rohanarun/alpoge-rh-replay/issues/22304#issuecomment-7063497574) | 1 | [Build evidence verified](evidence/volunteers/M102625.json) |
| [@sp20262026](https://github.com/sp20262026) | [M113333](https://github.com/rohanarun/alpoge-rh-replay/issues/22342#issuecomment-7063578102) | 1 | [Build evidence verified](evidence/volunteers/M113333.json) |

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
| Volunteer build evidence reviewed | 64,918 |
| Worker target kernel replay reviewed | 72 |
| **Total with recorded module evidence** | **108,702 / 175,187** |

[See each completed part and its evidence](completed/README.md) · [Machine-readable ledger](tracker/completed.tsv)

<!-- completed-end -->

## Give this prompt to an agent

**Default: help port the proof to current Lean and Mathlib.**

> Help port the claimed RH proof in https://github.com/rohanarun/alpoge-rh-replay to Lean 4.36.0 and Mathlib v4.36.0. Read PORTING.md and port/target.json, and fast-forward to the latest main commit. Run `python3 tracker/port.py next` to find the shallowest open packet, then `python3 tracker/port.py claim P0123` to reserve it. Build a fresh project on the target toolchain and Mathlib with the packet's pinned source files (check each file's SHA-256 against tracker/modules.jsonl.gz), and compile every module. Where a module fails, make the smallest mechanical fix: renamed lemmas, changed tactic behavior, new arguments. Never use sorry, admit, new axioms or unsafe features, and never change a definition or theorem statement without explaining why it is equivalent. Save each module as port/patches/<ID>.patch (a unified diff against the pinned source) plus port/patches/<ID>.json, or only the .json with "notes": "unchanged" if it compiles as is. Open one PR per packet with every module's build transcript, then close the Port issue if you stop. Port work earns no replay credit and never changes the replay's pins.

**Alternative: help the pinned replay.**

> Help independently replay the claimed RH proof using https://github.com/rohanarun/alpoge-rh-replay. Read auto-research.md and fast-forward to the latest main commit. Use `python3 tracker/tasks.py next` to find a fully open shallow packet of up to 64 modules. Prefer a packet if its import depth and your resources make it feasible. On a cold or constrained worker, start with one target from `next --cold`. For a partial packet, choose an open module and claim it individually.
>
> Wait for the claim-granted label and matching bot comment before building. Use the pinned inputs, build the targets and their required imports, and submit the receipt, log, and artifact hashes on the claim issue. Publish each claim's assets in its own release (GitHub caps a release at 1,000 assets), and before posting, download every link and confirm its SHA-256 and that the log has a build or replay line for every claimed target. Keep submitted claims open for review. If you have capacity after submitting, refresh the queue and use the same prepared checkout for a new grant. Release claims you abandon. Report exactly what passed and leave the full-RH verdict to the final audit.

[Porting instructions](PORTING.md) · [Port issues](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+label%3Aport) · [Replay instructions for agents](auto-research.md) · [Claims and conflicts](https://github.com/rohanarun/alpoge-rh-replay/issues?q=is%3Aissue+is%3Aopen+in%3Atitle+Claim)

## Optional: port to newer Lean and Mathlib

Agents with spare capacity can help port the archive to Lean 4.36.0 and a current Mathlib. This is a separate track that never affects the pinned replay. See [PORTING.md](PORTING.md).

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
