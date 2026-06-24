# skill-upgrade

I had a skill that worked. It did its job in most cases, and the temptation was
to tidy the prose, bump the number, and call it upgraded. Then I ran it against a
council of agents whose only instruction was to break it, and watched it perform
its own discipline convincingly, report itself compliant, and violate its own
rule anyway. That was the day I learned that "make it nicer" is not an upgrade.
An upgrade starts by naming where the skill breaks.

This is the process that took that skill from "works" to publish-grade, and past
it, written down so it runs on any behavioral skill, not just the one it came
from.

## Two rules that govern the whole thing

1. **An upgrade needs a what-for.** Do not upgrade for tidiness. Name what the
   current version gets wrong, who it hurts, and what a strangers-can-use-it
   version unlocks. No named gap, no upgrade.
2. **Eat the skill's own dogfood.** The process must obey the discipline of the
   skill it upgrades. Hardening a verification skill? Then every claim in the
   upgrade is itself grounded or marked unverified. A skill that cannot survive
   being applied to its own upgrade is not ready.

## First, triage the skill

Before any step, classify the skill: reflex, module, or engine. The class decides
how heavy the apparatus should be, so a forty-line reflex skill is not pushed
through the same pipeline as a full engine. A reflex skill skips the formal test
bank and the contribution infrastructure; an engine earns all of it. Do not build
apparatus the skill does not need.

## The seven steps (steps 5 to 7 only when publishing for others)

1. **Spec the gap, lock the architecture** before writing a word.
2. **Stress-test at scale**, convene an adversarial council whose job is to break
   it, then draw an explicit boundary: CUT, KEEP, FIX, ADD.
3. **Rewrite and anchor in real prior-art, community first**, never from memory.
   Write the methodology as a story with citations, including where it lost.
4. **Separate the universal engine from the context-bound parts** so culture or
   domain content does not squat in the canonical core.
5. **Formalize the test apparatus**: fixtures someone else can run, a frozen
   regression bank, a short tests README.
6. **Build contribution infrastructure that holds the bar without a gatekeeper**:
   a rubric that forces the standard, CI that enforces the mechanical rules.
7. **Audit, version, package.** Publishing is the author's hand.

The full step-by-step, with the worked example behind each one, is in `SKILL.md`.

## Going past 100%

Hitting the benchmark is steps one to seven. Exceeding it is one more move: find
the thing the benchmark skill does not do that this one can, and do it. The
strongest version is a skill that names its own ceiling, says where prose stops,
and specs the harness past it.

## Where this stops

This is a process, not a guarantee. It will make a skill honest and reproducible;
it cannot make a weak idea worth keeping, and it will not enforce itself if you
skip a step. The discipline is only as good as the hand running it, which is why
rule two exists: the process has to survive being applied to itself. It was
distilled from one real upgrade, so run it on your own skill and it will surface
failures these seven steps did not anticipate. That is the process working, not
failing.

## What this is not for

Do not run it on a skill with no named gap, or on a trivial fix that needs an edit,
not a process. The seven steps are for a real version jump.

## Install

    cp -R skill-upgrade ~/.claude/skills/

Reload your assistant. The `name` field becomes the trigger.

## Author

Le Cong Hoang (LCH). Apache-2.0, see `LICENSE`. Distilled from the
what-for-and-how v2 to v3.1 upgrade.
