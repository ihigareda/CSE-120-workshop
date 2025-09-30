<!--
Edit in place. Remove sections that do NOT apply. Keep signal high.
-->


## Summary <!-- Always Required -->
<!-- High–level: What changed + why now (1–3 sentences). -->

## Change Type Quick Pick <!-- Always Required -->
<!-- Tick ALL that genuinely apply -->
- [ ] Feature (new user-visible capability)
- [ ] Bug Fix (corrects incorrect behavior)
- [ ] Documentation Only
- [ ] Refactor (no functional change intended)
- [ ] Test Additions / Updates
- [ ] Performance Improvement
- [ ] Build / CI / Chore

---
## Context & Rationale <!-- Always Required -->
<!-- Deeper motivation, prior limitations, linked design discussions. -->

## Design / Approach Overview (Features & Refactors) <!-- New Feature PR / Refactor PR -->
<!-- Describe core idea, key data structures, algorithms, interface changes. -->
- Core idea:
- Data structures / algorithms:
- Interfaces added / changed:
- Alternatives considered (brief):

## Problem / Root Cause (Bug Fixes) <!-- Bug Fix PR -->
<!-- For fix PRs: what was broken? Root cause analysis. -->
- Symptom:
- Root cause:
- Why now / trigger:

## Implementation Notes <!-- Most PRs (Feature / Fix / Refactor / Perf) -->
<!-- Not obvious decisions, trade-offs, constraints, gotchas, follow-up deferrals. -->

## Before vs After (Refactors / Perf) <!-- Refactor PR / Performance PR -->
<!-- Structural diff summary; expected behavioral equivalence statement if refactor. -->
- Statement of intended behavior change (or none):
- Key structural differences:

## Tests <!-- Feature PR / Bug Fix PR / Refactor (safety) / Test PR -->
<!-- Summarize test impact. Remove subsections that don't apply. -->
### Added <!-- Test PR / Feature PR / Bug Fix PR -->
<!-- List new test files or cases -->
### Modified <!-- Test PR / Refactor PR (if adapting) / Bug Fix PR -->
### Removed (justify) <!-- Rare: cleanup / refactor / deprecation -->
### Coverage / Scenarios <!-- Test PR / Feature PR / Bug Fix PR -->
<!-- Enumerate critical paths / edge cases -->
- Edge case 1
- Edge case 2
- Edge case 3
### Determinism / Flakiness Checks <!-- Test PR / Concurrency / Timing Sensitive -->
<!-- Timing assumptions? Random seeds? Concurrency stress? -->

## Manual Verification <!-- Feature PR / Bug Fix PR / Refactor (sanity) -->
<!-- Commands, scripts, or steps a reviewer can run quickly. -->
```
# example
make test
```
Evidence / logs / screenshots (if UI):

## Performance (If Applicable) <!-- Performance PR / Large Feature / Optimization -->
<!-- Baseline vs new (qualitative or measured). Include methodology if measured. -->
- Benchmark / scenario:
- Before:
- After:
- Method / tool:
- Regression risk:

## Documentation Updates <!-- Documentation PR / Feature PR / Refactor (API changes) -->
<!-- List docs touched; ensure they're committed or linked. -->
- [ ] README
- [ ] Design doc
- [ ] Inline comments
- [ ] Diagrams / images
- [ ] Course / lab instructions
Notes:

## Verification of No Functional Change (Refactors Only) <!-- Refactor PR -->
<!-- Evidence: identical outputs, golden files, logs, diff tools, etc. -->

## Follow-Ups / Deferred Work <!-- Optional / Roadmap Notes -->
<!-- Future improvements enabled or consciously postponed. -->

## Related / Linked Issues <!-- Always Required (unless truly none) -->
<!-- "Closes issue <n>" for automatic closure. Multiple lines allowed. -->
Closes issue 
Related:

## Related PRs / Docs <!-- Cross-Repo / Split Work / Docs -->
<!-- Cross-references to dependent or documenting PRs. -->

---
## Checklist <!-- Always Required -->
<!-- Keep only relevant; all checked items should be true before merge. -->
- [ ] Semantic title follows convention
- [ ] Issue(s) linked (or rationale if none)
- [ ] Tests added / updated / unchanged rationale
- [ ] All tests pass locally
- [ ] Lint / style passes (if applicable)
- [ ] No dead / debug / commented-out code
- [ ] Docs updated or not needed (explained)
- [ ] No functional change (if refactor) explicitly stated & verified
- [ ] Performance characteristics acceptable / evaluated (if relevant)
- [ ] No flaky tests introduced
- [ ] Follows course integrity guidelines

---
## Reviewer Guidance (Optional) <!-- Complex / Risky Changes -->
<!-- Call out areas where focused review is most valuable (complex logic, concurrency, edge cases). -->

## Additional Notes <!-- Risks / Assumptions / Rollback Plan -->
<!-- Anything else: risks, assumptions, rollback plan. -->