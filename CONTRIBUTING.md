# Contributing to skill-upgrade

This skill holds its bar without a human gatekeeper. A contribution is accepted
when it passes the checks below, which are themselves an instance of the skill's
own discipline. Run `python3 scripts/validate_skill.py .` before you open a pull
request; CI runs the same check.

## The rubric (each item is the skill applied to your change)

1. **Name the what-for.** State, in three fields, what the current version gets
   wrong, who it hurts, and what your change unlocks. A change with no named gap
   is declined, the same brake the skill puts on every upgrade.
2. **Triage your change.** Say which class of skill it affects and why the
   apparatus you add or remove fits that class. Do not add engine-weight to a
   reflex-class concern.
3. **Ground your claims.** Any factual claim (a tool behaves a certain way, a
   practice is standard) carries a source you consulted, added to the sources
   ledger in `METHODOLOGY.md`. No claim from memory.
4. **Bring the test.** A new rule or guard comes with a fixture in
   `tests/cases.json` that fails without your change and passes with it
   (test-first). A change with no test that could catch its regression is
   incomplete.
5. **Self-check.** Confirm: no em-dash, frontmatter intact, versions consistent
   across SKILL, CITATION, and CHANGELOG, and the validator green.

## What the validator enforces (so a human need not)

`scripts/validate_skill.py` checks the mechanical bar: the required artifact set
for the class is present, no banned characters, frontmatter has name and version,
the three versions agree, and `METHODOLOGY.md` carries its load-bearing sections.
`--selftest` proves the checker catches each cheat the original council found.

## What it cannot enforce

Judgment. The validator confirms your methodology section exists; it cannot
confirm your reasoning is sound or your sources support your claims. That review
is human, and it is the one part of the bar a script does not hold.
