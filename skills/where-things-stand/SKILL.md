---
name: where-things-stand
description: Reconstruct current state from Grain meetings over time. Use when the user asks where things stand or what the latest is on an account, project, topic, or person, wants to catch up after time away, or asks about their recent recorded meetings ("what was my last meeting?", "who did I meet with this week?").
argument-hint: "<account, project, topic, or time window>"
---

# Where Things Stand

**Fold** the conversations about X over time into: current state, what changed, what's open. Not a meeting-by-meeting recap — the user wants to be current, not comprehensive.

Read first:
- `${CLAUDE_PLUGIN_ROOT}/references/retrieval.md` — scoping defaults, cheap-layers-first, latency discipline
- `${CLAUDE_PLUGIN_ROOT}/references/evidence.md` — supersession, conflicts, coverage honesty

## Workflow

1. **Scope fast.** Account/person-first; default windows per the retrieval playbook. This is the plugin's slowest operation — narrow-and-stated now beats broad-and-slow.
2. **Read notes chronologically**, newest last, so supersession is visible. Action items for what's open; transcript search only to fill specific gaps.
3. **Fold.** Distinguish decided vs. discussed vs. mentioned — state reconstruction dies when discussion gets promoted to decision. Done when every open item has an owner and source, and every reversal is noted.

## Output

```text
Where things stand: [scope, window covered]

Current state:
- ...

What changed:
- ... (meeting, date, link)

Open:
- ... (owner, source)

Worth opening:
- [meeting, date, link] — why
```

Readable in under two minutes; drop empty sections. "Nothing significant changed" is a legitimate, complete answer when true.
