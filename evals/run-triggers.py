#!/usr/bin/env python3
"""Trigger-routing regression suite.

Runs each prompt in trigger-cases.json against the plugin headlessly and
asserts which skill (if any) fires. Exit 0 = all pass, 1 = any fail.

Usage:
    python3 evals/run-triggers.py [--case NAME] [--jobs N]

Requires: claude CLI on PATH. Run from anywhere; paths resolve relative to
this file. Each case costs one short model call (~30-60s); cases run in
parallel. When `claude plugin eval` exits early access, migrate these cases
to evals/**/case.yaml and delete this runner.
"""
import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
NAMESPACE = "meeting-memory-by-grain:"


def fired_skills(prompt: str) -> list[str]:
    proc = subprocess.run(
        [
            "claude", "--plugin-dir", str(PLUGIN_DIR), "-p", prompt,
            "--output-format", "stream-json", "--verbose",
            "--max-turns", "2", "--allowedTools", "Skill",
        ],
        capture_output=True, text=True, timeout=300,
    )
    skills = []
    for line in proc.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") != "assistant":
            continue
        for block in ev.get("message", {}).get("content", []):
            if block.get("type") == "tool_use" and block.get("name") == "Skill":
                skills.append(block["input"].get("skill", "").removeprefix(NAMESPACE))
    return skills


def run_case(case: dict) -> tuple[dict, list[str], bool]:
    fired = fired_skills(case["prompt"])
    expect = case["expect"]
    ok = (not fired and not expect) or bool(fired and fired[0] in expect)
    return case, fired, ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", help="run only cases whose name contains this string")
    ap.add_argument("--jobs", type=int, default=6)
    args = ap.parse_args()

    cases = json.loads((Path(__file__).parent / "trigger-cases.json").read_text())["cases"]
    if args.case:
        cases = [c for c in cases if args.case in c["name"]]
    if not cases:
        print("no cases matched", file=sys.stderr)
        return 1

    failures = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for case, fired, ok in pool.map(run_case, cases):
            mark = "PASS" if ok else "FAIL"
            failures += not ok
            expected = " or ".join(case["expect"]) or "(none)"
            actual = ", ".join(fired) or "(none)"
            print(f"{mark}  {case['name']:28s} expected: {expected:30s} fired: {actual}")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
