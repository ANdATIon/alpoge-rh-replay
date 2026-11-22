# Agent Instructions — Lean 4.36 Proof Optimization

> **Notice:** The Lean `v4.36.0` port of Alpöge's Riemann Hypothesis proof is **complete**. Do **not** claim legacy packets (`Claim P####` / `Claim M######`) or open Lean 4.33 → 4.36 porting PRs in `rohanarun/alpoge-rh-replay`.

## Target Codebase

Work on the consolidated Lean `v4.36.0` + Mathlib (`fc4f59e577feb1a4956671bc04ac18aaaf8cd842`) codebase:
- **Upstream repository:** https://github.com/leanprover-community/riemann-hypothesis (`main`)
- **Consolidated 47,882-module branch (`−67.95%` file count vs `main`):** https://github.com/leanprover-community/riemann-hypothesis/pull/120 (`rohanarun/riemann-hypothesis`, branch `opt/collapse-and-consolidate-4.36`)

## Optimization Priorities

Focus on self-contained, verifiable improvements to the Lean 4.36 proof:
1. **Import & dependency pruning:** Remove unused transitive imports, flatten remaining single-declaration pass-through wrappers, and shorten import depth.
2. **Proof & tactic acceleration:** Speed up slow modules, replace heavy `simp` / `aesop` / `linarith` / `omega` scripts with direct rewrites or lemmas, and eliminate `set_option maxHeartbeats` bumps where possible.
3. **Mathlib deduplication & modularization:** Replace duplicated local helper definitions or lemmas with canonical Mathlib `v4.36.0` declarations, and decompose overly large files cleanly without re-creating wrapper chains.

## Strict Verification Rules

- **Never modify** `src/Challenge.lean`, `src/Statements.lean`, or `comparator.json`.
- **Never introduce** `sorry`, `admit`, new `axiom`s, or unsafe features.
- Verify every modified module with `lake build <Target>` (and `lake build Main Challenge` + `lake comparator` for end-to-end PRs).
- Include before/after build times, import counts, and `.olean` sizes in your PR description.

---

*Historical Lean 4.33.1 replay documentation is preserved in git history and [STATUS.md](STATUS.md).*
