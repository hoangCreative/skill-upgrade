#!/usr/bin/env python3
"""Validate a behavioral-skill package against its triage class.

Engine-class skills (the default) must ship the full apparatus and pass the
mechanical checks below. `--selftest` runs the bundled cases in tests/cases.json
to prove the checker catches each cheat the v2 adversarial council found.

The banned em-dash character is referenced as chr(0x2014) so this source file
itself contains none (a repo hook bans the literal byte).
"""
import json
import os
import re
import sys

EMDASH = chr(0x2014)

ENGINE_REQUIRED = [
    "SKILL.md", "README.md", "METHODOLOGY.md", "CHANGELOG.md",
    "CITATION.cff", "LICENSE", "CONTRIBUTING.md",
    "tests/README.md", "tests/cases.json",
    "scripts/validate_skill.py",
]

# CI is recommended, not required: a repo pushed by an OAuth app cannot include
# a .github/workflows file without the workflow scope, so its absence is a
# warning, not a failure. The validator script itself is the enforceable bar.
ENGINE_RECOMMENDED = [".github/workflows"]

METHODOLOGY_SECTIONS = ["what for", "boundary", "sources", "dogfood", "limit"]

VERSION_RE = r'(?m)^version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?'


def evaluate(state):
    """Pure verdict over a normalized state dict. Returns (ok, problems)."""
    problems = []
    klass = state.get("klass", "engine")
    required = ENGINE_REQUIRED if klass == "engine" else ["SKILL.md", "README.md"]
    present = set(state.get("files", []))
    missing = [f for f in required if f not in present]
    if missing:
        problems.append("missing required artifacts: " + ", ".join(missing))
    if state.get("emdash", 0) > 0:
        problems.append("em-dash present (%d)" % state["emdash"])
    if not state.get("has_name"):
        problems.append("frontmatter missing name")
    if not state.get("has_version"):
        problems.append("frontmatter missing version")
    versions = [v for v in (state.get("v_skill"), state.get("v_citation"),
                            state.get("v_changelog")) if v is not None]
    if len(set(versions)) > 1:
        problems.append("version mismatch: " + " / ".join(versions))
    if klass == "engine":
        secs = [s.lower() for s in state.get("methodology_sections", [])]
        miss = [s for s in METHODOLOGY_SECTIONS if not any(s in x for x in secs)]
        if miss:
            problems.append("methodology missing sections: " + ", ".join(miss))
        if not state.get("boundary_has_cut"):
            problems.append("boundary drawn without a CUT (anti-bloat not exercised)")
        if state.get("dogfood_claimed") and not state.get("dogfood_record"):
            problems.append("dogfood claimed without a record")
        if state.get("ceiling_claimed") and not state.get("ceiling_harness_spec"):
            problems.append("ceiling claimed without a concrete harness spec")
    warnings = []
    if klass == "engine":
        warnings = ["recommended artifact absent: " + f
                    for f in ENGINE_RECOMMENDED if f not in present]
    return (len(problems) == 0, problems, warnings)


def _read(base, rel):
    try:
        with open(os.path.join(base, rel), encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def scan_package(base):
    """Build a normalized state from a real skill folder on disk."""
    files = set()
    for root, _dirs, names in os.walk(base):
        for name in names:
            files.add(os.path.relpath(os.path.join(root, name), base))
    norm = set()
    for must in ["SKILL.md", "README.md", "METHODOLOGY.md", "CHANGELOG.md",
                 "CITATION.cff", "LICENSE", "CONTRIBUTING.md",
                 "tests/README.md", "tests/cases.json",
                 "scripts/validate_skill.py"]:
        if must in files:
            norm.add(must)
    if any(r.startswith(".github/workflows") and r.endswith((".yml", ".yaml"))
           for r in files):
        norm.add(".github/workflows")
    emdash = 0
    for rel in files:
        if rel.endswith((".md", ".py", ".cff", ".yml", ".yaml")):
            emdash += _read(base, rel).count(EMDASH)
    skill = _read(base, "SKILL.md")
    citation = _read(base, "CITATION.cff")
    changelog = _read(base, "CHANGELOG.md")
    methodology = _read(base, "METHODOLOGY.md")
    v_skill = re.search(VERSION_RE, skill)
    v_cit = re.search(VERSION_RE, citation)
    v_chg = re.search(r'(?m)^##\s*\[([0-9]+\.[0-9]+\.[0-9]+)\]', changelog)
    meth_low = methodology.lower()
    return {
        "klass": "engine",
        "files": sorted(norm),
        "emdash": emdash,
        "has_name": bool(re.search(r'(?m)^name:\s*\S', skill)),
        "has_version": v_skill is not None,
        "v_skill": v_skill.group(1) if v_skill else None,
        "v_citation": v_cit.group(1) if v_cit else None,
        "v_changelog": v_chg.group(1) if v_chg else None,
        "methodology_sections": re.findall(r'(?m)^#{1,3}\s*(.+)$', methodology),
        "boundary_has_cut": ("cut" in meth_low and "boundary" in meth_low),
        "dogfood_claimed": "dogfood" in (skill + methodology).lower(),
        "dogfood_record": "dogfood record" in meth_low,
        "ceiling_claimed": False,
        "ceiling_harness_spec": False,
    }


def run_selftest(here):
    path = os.path.join(here, "tests", "cases.json")
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    base = data["base"]
    wrong = 0
    for case in data["cases"]:
        state = dict(base)
        state.update(case.get("override", {}))
        ok, _problems, _warnings = evaluate(state)
        want = case["expect"] == "pass"
        good = ok == want
        wrong += 0 if good else 1
        mark = "OK  " if good else "WRONG"
        print("  [%s] %-32s expect=%s got=%s" % (
            mark, case["name"], case["expect"], "pass" if ok else "fail"))
    print("selftest: %d case(s), %d wrong" % (len(data["cases"]), wrong))
    return 0 if wrong == 0 else 1


def main(argv):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--selftest" in argv:
        return run_selftest(here)
    target = next((a for a in argv[1:] if not a.startswith("-")), ".")
    ok, problems, warnings = evaluate(scan_package(target))
    for w in warnings:
        print("  ! " + w)
    if ok:
        print("validate: OK (%s)" % target)
        return 0
    print("validate: FAIL (%s)" % target)
    for p in problems:
        print("  - " + p)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
