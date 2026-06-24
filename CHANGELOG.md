# Changelog

All notable changes to this skill. Format follows Keep a Changelog; versions are semantic.

## [2.0.0] - 2026-06-24

The dogfood release. `skill-upgrade` was run on itself: triaged engine-class,
stress-tested by a three-voice adversarial council, and brought to the full
publish-grade apparatus it had been asking other skills to build but lacked. The
bump is MAJOR: a mandatory Step 0 triage now reshapes how the process runs.

### Added
- Step 0 triage gate: classify the skill (reflex / module / engine) so the
  apparatus scales to its size and reach.
- A checkable artifact per step, with the version bump gated on a checklist of
  them, closing the self-report hole an adversarial review found.
- `METHODOLOGY.md`: the design account, the council story, the cut/keep/fix/add
  boundary, the sources ledger, and the dogfood record.
- `tests/` (cases plus README) and `scripts/validate_skill.py` with a `--selftest`
  that proves the checker catches each council-found cheat; a CI workflow.
- `CONTRIBUTING.md`: a rubric that is itself an instance of the skill's discipline.
- Prior-art anchoring: SemVer, Keep a Changelog, ADRs, RFC 2119, red-teaming, TDD,
  golden-master tests, LLM-as-judge caveats, dogfooding, and the host's own
  agent-skill and eval guidance.

### Changed
- the seven steps are reorganized into a core (1 to 4, always run) and a publish
  track (5 to 7, entered only when publishing for others), each scaled by class.
- "Going past 100%" is gated to engine-class and requires a concrete harness spec,
  not a vague mention.
- step 2's council now requires independence, at least one new failure, and at
  least one CUT; discovered failures become failing fixtures before the rewrite.

### Removed
- the implicit assumption that every skill ships the full document set regardless
  of size.

## [1.0.0] - 2026-06-24

First release. The seven-step upgrade process distilled from the what-for-and-how v2 to v3.1 upgrade (notes 149 and 153), generalized to run on any behavioral skill.

- Two governing rules: an upgrade needs a what-for; the process must obey the upgraded skill's own discipline.
- Seven steps: spec and lock architecture; stress-test plus adversarial council plus cut/keep/fix/add boundary; rewrite and anchor in prior-art; separate engine from context; formalize tests; contribution infrastructure without a gatekeeper; audit and version.
- A "past 100%" move: make the skill name its own ceiling and spec the harness beyond prose.
- First real application: ground-or-abstain v2.2.1 to v2.3.0.
