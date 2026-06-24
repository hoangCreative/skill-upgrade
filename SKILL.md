---
name: skill-upgrade
version: "2.0.0"
description: >
  Use when taking an existing behavioral skill from "works" to publish-grade and beyond. A triage-gated,
  scale-aware process: first classify the skill (reflex / module / engine) so the apparatus fits its size,
  then run a core (spec the gap, stress-test with an adversarial council and a cut/keep/fix/add boundary,
  rewrite and ground every claim in real prior-art community-first, separate the universal engine from
  context-bound parts) and, only when publishing for others, a publish track (formalize tests, build
  contribution infrastructure that holds the bar without a gatekeeper, audit and version). Every step leaves
  a checkable artifact and the version bump is gated on them. Two governing rules: an upgrade needs a
  what-for, and the process must eat its own dogfood. Explicit triggers: skill-upgrade, upgrade this skill,
  take this skill to publish grade, harden this skill.
metadata:
  author: Le Cong Hoang (LCH)
  copyright: "© 2026 Le Cong Hoang"
  created: "2026-06-24"
  updated: "2026-06-24"
  origin: distilled from the what-for-and-how v2 to v3.1 upgrade, then hardened by running this process on itself
---

# skill-upgrade

A process for taking a behavioral skill that already works to publish-grade, and past it. Not "make it
nicer." It finds where the skill breaks under pressure, grounds it in real practice, and builds only as much
scaffolding as the skill's size and reach actually warrant.

The first version made one mistake it now guards against: it generalized the full weight of a large engine's
upgrade onto every skill, so a forty-line reflex skill got pushed toward a thousand-case stress test and a CI
pipeline it would never use. v2 fixes that with a triage gate, and closes the deeper hole an adversarial
review found: most steps left nothing on disk, so "I ran the process" was pure self-report. Now every step
leaves a checkable artifact, and the version bump is gated on them.

## Two rules that govern the whole thing

1. **An upgrade needs a what-for.** Do not upgrade for tidiness. Name what the current version gets wrong,
   who it hurts, and what a strangers-can-use-it version unlocks, as three concrete fields, not a tone. No
   named gap, no upgrade.
2. **Eat the skill's own dogfood, and prove it.** The process must obey the discipline of the skill it
   upgrades, and leave a DOGFOOD record that names that discipline and shows one concrete instance per
   claim-class where the upgrade obeyed it. A dogfood claim with no record does not count. (This skill's own
   record lives in `METHODOLOGY.md`.)

## Step 0: Triage before anything (the gate)

Classify the skill first. The class decides how heavy the apparatus is, so the process fits the skill
instead of crushing it.

| Class | Looks like | Steps 2 / 5 / 6 / past-100 |
|---|---|---|
| **Reflex** | one rule, a few triggers, no branching (e.g. "search the community before you debug") | LITE / SKIP / SKIP / SKIP |
| **Module** | several rules or one decision branch, some interpretive judgment | LITE-to-FULL / LITE / conditional / SKIP |
| **Engine** | branching logic, interpretive judgment, meant for outside use | FULL / FULL / FULL / allowed |

Two axes set the class: **size and branching** (how much can silently break) and **reach** (will anyone but
the author run or extend it). A skill earns the full publish track only if it is actually published for
others; a private reflex skill that earns an upgrade still does not earn CI and a citation file. Record the
class and the chosen levels before any other step. This gate is the modern form of spec-first design (PEP-1)
and uses MUST / SHOULD / MAY (RFC 2119) for the levels.

The escape-hatch pattern comes from the old step 4 and now governs every step: **do not build apparatus this
skill does not need.**

## The core: steps 1 to 4 (always run, scaled to the class)

### 1. Spec the gap, lock the architecture
Before writing a word: name the gap as three labeled fields (current-failure / who-is-hurt / what-unlocks),
and decide and lock the new architecture. Write the decision down ADR-style (context, decision, consequence)
so the rationale survives. Output: a committed gap-spec and architecture note (consolidating them in
`METHODOLOGY.md` is fine).

### 2. Stress-test, convene an adversarial council, draw the boundary
This is LLM red-teaming: probe the skill with adversarial inputs to find failures before release. Scale it
to the class. A reflex skill gets five to ten trigger / anti-trigger examples and one independent reviewer
trying to make the rule misfire; an engine gets a wide case matrix (vary domain, context, shape, language)
and a multi-voice council. Requirements that stop the step from becoming theatre:
- the reviewers are independent of the author (distinct agents or people), named in the output;
- the case matrix is committed as data;
- the council surfaces at least one NEW failure mode; a council that finds nothing is treated as one that
  did not run, not as a pass;
- the boundary is drawn explicitly as CUT / KEEP / FIX / ADD, with at least one CUT (quote the removed text)
  or a signed line defending why nothing was cut.

Then, test-first: each FIX-tagged failure becomes a written failing fixture BEFORE the rewrite
(red-green-refactor), not a fixture reconstructed afterward.

### 3. Rewrite and anchor in real prior-art, community first
Rewrite to the locked architecture. Ground every load-bearing claim in literature or community practice
searched this turn, never asserted from memory, and keep a sources ledger: one row per claim with its URL
and retrieval date. Write the methodology as a story that includes where the skill lost. A methodology that
hides its failures is advertising, not method. The single most on-point body of prior-art for a behavioral
skill is the host's own skill-authoring and evaluation guidance; anchor there rather than claiming pure
invention.

### 4. Separate the universal engine from the context-bound parts
Pull the universal mechanism into the core. Split culture- or domain-bound content into a labeled,
detachable pack so it does not squat in the canonical engine. If the skill is genuinely universal, confirm
monolithic is right and say so. Do not invent a pack architecture a universal skill does not need.

## The publish track: steps 5 to 7 (only when publishing for others)

Enter this track only if the triage class says so. A private upgrade can stop after the core.

### 5. Formalize the test apparatus
Make the testing reproducible: structured fixtures (good and bad cases as data), a frozen regression bank
with one fixture per FIX-failure from step 2, and a short tests README. These are golden-master /
characterization tests: they pin observed behavior and flag any change for a human to judge. Their known
limit, stated plainly: freezing behavior is not freezing correctness, so a bank can lock in a bad call. The
validation script must actually run the fixtures, and a green run gates the version bump.

### 6. Build contribution infrastructure that holds the bar without a gatekeeper
A CONTRIBUTING guide, a mandatory rubric that forces the standard (sourced claims, included tests, a
self-check), and CI plus a validation script that enforce the mechanical rules on every change. Two cautions
from practice: the rubric is an LLM-as-judge, and judges run lenient and biased, so it must be calibratable
and its bias named, not trusted to rubber-stamp; and CI is the un-skippable server-side gate, a local hook
is not enough. Where it fits, the rubric should itself be an instance of the skill's discipline.

### 7. Final audit, version, package
Audit against a checklist that FAILS if any artifact the class requires is missing (gap-spec, council
boundary with its CUT, sources ledger, dogfood record, tests, CI, README, CHANGELOG, CITATION, LICENSE).
Fix the mechanical failures (banned characters, leaked secrets, license and version consistency, internal
contradictions). Choose the bump by SemVer (a removed or renamed rule is MAJOR, a backward-compatible
addition is MINOR, a fix is PATCH) and write the entry in Keep a Changelog form. The version bump is the
LAST action, blocked until the checklist is green.

## Going past 100% (engine-class only, and gated)

Exceeding the benchmark is one more move: find what the benchmark skill does NOT do that this one can, and
do it. The strongest version names its own ceiling. But name a ceiling only with a concrete harness spec an
implementer could build from: the inputs, the check it runs, and why prose cannot close it. A vague "a
runtime harness would help" earns nothing, and is itself the speculative over-engineering this process
guards against.

## What this is not for

Do not run this on a skill with no named gap, or on a trivial fix (a typo, one banned word) that needs an
edit, not a process. Earning an upgrade and deserving the full apparatus are two different questions; Step 0
answers the second.

## The honest limit of this skill

A checker can verify an artifact EXISTS and has the right shape; it cannot verify the artifact is GOOD. The
process enforces presence and form, not judgment. And the triage class is self-declared, so an author can
mislabel an engine as a reflex to dodge the apparatus; the final audit reduces that but does not close it.
This skill makes an upgrade honest and legible. It does not make a weak skill worth keeping.

## Prior-art this process stands on

Spec-first and net-improvement gate (PEP-1), requirement levels MUST/SHOULD/MAY (RFC 2119), Architecture
Decision Records (Nygard), red-teaming and adversarial evaluation (OWASP LLM Top 10, promptfoo), test-first
red-green-refactor (Beck), golden-master / characterization tests (Feathers), LLM-as-judge with its
calibration caveat, dogfooding (Microsoft, 1988), Semantic Versioning, Keep a Changelog, and the host's own
agent-skill authoring and eval-driven-development guidance. Full citations with URLs are in `METHODOLOGY.md`.

## Sibling

This is the upgrade-time companion to the factory blueprint for `pattern-to-skill` (making a NEW skill from
a raw habit). That factory makes a skill exist; this process takes an existing skill to publish-grade and
beyond.
