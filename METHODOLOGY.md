# Methodology: skill-upgrade

This is the design account for `skill-upgrade`, written as the skill's own step 3
demands: a story that includes where it lost, with every load-bearing claim
grounded in a source. It doubles as the record that steps 1, 2, and 7 require to
exist on disk, and as the dogfood proof for governing rule 2.

## 1. What for (the gap that earned the v2 upgrade)

- **Current failure:** v1 was a flat seven-step process distilled from upgrading
  one large engine (`what-for-and-how`). It generalized that engine's weight onto
  every skill, and it left most steps with no artifact on disk, so "I ran the
  process" was unverifiable self-report. The skill diagnosed exactly this disease
  in its predecessor and then reproduced it.
- **Who is hurt:** an author with a small reflex skill, pushed to build a
  thousand-case stress test and a CI pipeline it will never use; and any reader
  who cannot tell a real upgrade from a theatrical one, because nothing is
  checkable.
- **What a strangers-can-use-it version unlocks:** a process that fits the skill
  it runs on, leaves a checkable trail, and can be pointed at itself.

## 2. The architecture decision (locked before rewriting)

Decision: add a triage gate (Step 0) that classifies the skill and scales the
apparatus, reorganize the seven steps into a core (1 to 4, always) and a publish
track (5 to 7, conditional on outside use), and require every step to leave a
committed artifact, with the version bump gated on a checklist of them.

Recorded ADR-style (Nygard): the gate resolves a real tension surfaced in the
council (section 3), and the cost is one more mandatory step, accepted because it
removes far more downstream waste than it adds.

## 3. How it was stress-tested (the adversarial council)

Three independent reviewers, each a distinct agent, each told to break the skill,
not bless it. None was the author. The case under test was the v1 `SKILL.md` and
`README.md`.

- **Gameability lens** found the dogfood rule and four of seven steps were
  unfalsifiable self-report; the highest-value fix was to force every step to
  leave a checkable file and gate the version bump on them.
- **Over-engineering lens** found the seven steps bore a large engine's weight and
  pushed bloat onto small skills; the cure already existed inside step 4 ("do not
  invent a pack a universal skill does not need") and needed propagating to every
  step behind a triage gate.
- **Prior-art lens** found the process presented established practice as private
  invention, and supplied the sources in section 6.

The two action lenses appeared to conflict, one demanding more mandated artifacts,
one demanding fewer. They are reconciled by the triage gate: the class sets the
apparatus size, and within that size every step stays checkable.

## 4. The boundary (cut / keep / fix / add)

- **KEEP:** the no-named-gap brake and "what this is not for"; the dogfood rule as
  the moral spine; step 4's self-limiting clause as the model for every step.
- **ADD:** Step 0 triage; a committed artifact per step; a DOGFOOD record; a
  sources ledger; council-independence, at-least-one-new-failure, and
  at-least-one-CUT requirements; a gated version bump; the prior-art anchors.
- **FIX:** steps 2, 5, 6, 7 and "past 100%" made conditional on the class;
  test-first ordering (failures become fixtures before the rewrite); the rubric
  treated as a biased LLM-judge needing calibration; CI as the un-skippable gate.
- **CUT:** the implicit assumption that every skill ships the full document set
  and a methodology-as-story; the unconditional "spec a runtime harness"
  invitation, demoted to engine-class and gated on a concrete spec.

At least one real CUT, as the skill's own step 2 requires: the unconditional
full-document-set expectation was removed.

## 5. The dogfood record (governing rule 2)

The discipline `skill-upgrade` must obey is its own. Each rule, with the instance
that proves this upgrade obeyed it:

- *An upgrade needs a what-for:* section 1 names the gap as three fields.
- *Triage before apparatus:* skill-upgrade is engine-class (a branching process,
  meant for outside use), so it earns the full publish track; recorded here, not
  assumed.
- *Stress-test with an independent council:* section 3, three distinct agents, at
  least one new failure each.
- *Ground every claim, community first:* section 6 is the sources ledger.
- *Every step leaves a checkable artifact:* this file is that artifact for steps 1
  to 4; `tests/`, `scripts/`, `CONTRIBUTING.md`, `.github/` for steps 5 to 7.
- *Version bump is last and gated:* `scripts/validate_skill.py` checks the
  artifact set and version consistency, and is run before the bump to 2.0.0.

## 6. Sources ledger

Gathered by the prior-art review in this upgrade's step 2 (searched at the time,
not asserted from memory). Each row: what it is cited for, source.

- Spec-first and net-improvement gate: PEP 1, https://peps.python.org/pep-0001/
- Requirement levels MUST/SHOULD/MAY: RFC 2119, https://datatracker.ietf.org/doc/html/rfc2119
- Architecture Decision Records: Nygard, https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
- Adversarial evaluation and red-teaming: promptfoo, https://www.promptfoo.dev/docs/red-team/ ; OWASP LLM Top 10, https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-llms
- Test-first red-green-refactor: TDD, https://en.wikipedia.org/wiki/Test-driven_development ; Fowler, https://www.martinfowler.com/bliki/TestDrivenDevelopment.html
- Golden-master and characterization tests, with the freeze-is-not-correctness caveat: https://en.wikipedia.org/wiki/Characterization_test
- LLM-as-judge, with the leniency and bias caveat: https://deepeval.com/guides/guides-llm-as-a-judge
- Contribution governance: GitHub CONTRIBUTING guidance, https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
- Dogfooding (origin, Microsoft 1988): https://en.wikipedia.org/wiki/Eating_your_own_dog_food
- Semantic Versioning: https://semver.org/spec/v2.0.0.html
- Keep a Changelog: https://keepachangelog.com/en/1.0.0/
- Closest prior-art, host guidance: Anthropic Agent Skills, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills ; eval-driven development, https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

UNVERIFIED: the aphorism "lower the barrier but hold the bar" was not found as a
single attributable source; treat it as a synthesis of the contribution-governance
and CI sources, not a citable term.

## 7. Honest limits

A checker verifies an artifact EXISTS and has the right shape; it cannot verify
the artifact is GOOD. The process enforces presence and form, not judgment. The
triage class is self-declared, so an author can mislabel an engine as a reflex to
dodge the apparatus; the final audit reduces this but does not close it. And the
sources here were gathered by an agent's search in this turn; they are cited as
found, not independently re-fetched claim by claim. This skill makes an upgrade
honest and legible. It cannot make a weak skill worth keeping.
