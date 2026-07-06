---
name: prep-me
description: Prepare the user for an upcoming conversation using Grain meeting history. Use when the user asks for prep or a briefing on a meeting, person, or account.
argument-hint: "<meeting, person, account, or project>"
---

# Prep Me

Orient the user before a conversation: where things stand with these people, what's owed in both directions, what to raise, what to avoid stepping on. **Oriented, not buried** — quick prep fits on one screen.

Read first:
- `${CLAUDE_PLUGIN_ROOT}/references/retrieval.md` — entity resolution, account-first scoping
- `${CLAUDE_PLUGIN_ROOT}/references/evidence.md` — fact vs. read

## Workflow

1. **Resolve who and what.** `search_persons` / `search_companies` for the counterpart; prior meetings with the same people or account. No calendar access — if the target is unclear, ask for the meeting title or participants (the one question worth asking here).
2. **Recover what matters for the next 30 minutes of that person's life:** where things stand, what we promised them and they promised us (check action items — walking in unaware of your own open commitment is the prep failure that hurts most), open questions from last time, sensitivities raised, and anything they said that deserves acknowledgment. For account prep, start with `get_dossier_for_company`; enrich with `fetch_deal` / `fetch_collection` when present.
3. Done when every open commitment between the user and the counterpart appears in the brief, and every "worth raising" / "careful with" item is marked as your read, not meeting fact.

## Output

```text
Prep: [meeting / person / account]

Where it stands: ...

Open between you:
- You owe them: ...
- They owe you: ...

Worth raising:
- ...

Careful with:
- ...

Sources: [meetings, dates, links]
```
