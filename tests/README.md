# Tests for skill-upgrade

The apparatus this skill's own step 5 requires, applied to the skill itself.

## What is here

- `cases.json`: a bank of cases, one good and several bad, each a normalized
  "upgrade state" plus the verdict the checker should return. The bad cases are
  the exact cheats the v2 adversarial council found: a version bumped with a
  missing methodology, a boundary with no CUT, a ceiling claimed with no harness
  spec, a dogfood claim with no record, an em-dash, and a version mismatch.

## How to run

    python3 scripts/validate_skill.py --selftest      # prove the checker catches each cheat
    python3 scripts/validate_skill.py .               # validate this package on disk

A regression is any case in `cases.json` whose checker verdict no longer matches
its expected verdict, or any new real package the checker passes when it should
fail.

## The known limit (characterization tests)

This bank is a golden-master suite: it pins the checker's behavior so a change
that breaks it is caught. Like all characterization tests, it freezes behavior,
not correctness. A case frozen with a wrong expectation would lock in the wrong
verdict. The fix for that is human review of the bank, not more cases.
