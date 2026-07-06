---
name: what-do-i-owe
description: Recover open commitments from Grain meetings — a ledger of what the user owes, what others owe them, and unowned loose ends. Use when the user asks about their action items or promises, what others committed to, or runs a sweep (weekly review, back from time off, before a 1:1).
argument-hint: "<person, account, project, or time window>"
---

# What Do I Owe

A commitment **ledger** across meetings. Grain already lists per-meeting action items — this skill's value is what the app doesn't do: aggregate across meetings, dedupe, separate mine-from-theirs, and flag what's probably stale.

Read first:
- `${CLAUDE_PLUGIN_ROOT}/references/retrieval.md` — scoping
- `${CLAUDE_PLUGIN_ROOT}/references/evidence.md` — confidence, staleness, no invented tasks

## Workflow

1. **Scope.** `myself` for identity; default window 7 days (30 for post-vacation or "everything open"). State the window.
2. **Pull commitment signals**, in reliability order: `fetch_meeting_action_items` (assignee, due date, status), notes sections about next steps and follow-ups, then `search_in_transcripts` for commitment language ("I'll", "we need to", "can you", "by Friday") to catch what extraction missed.
3. **Build the ledger.** Dedupe (the same commitment in notes and transcript is one item); group into owed-by-user / owed-to-user / unowned. Done when every listed item traces to a specific utterance or extracted action item — nothing plausible-but-unsourced survives.

## Output

```text
Open commitments ([window], [scope]):

You owe:
- [action] — [due if known] (meeting, date, link) [confidence if not explicit]

Owed to you:
- [who]: [action] — (source)

Loose ends (no clear owner):
- ...
```

## Specific to this skill

- Never create or update tasks in any external system without explicit confirmation.
