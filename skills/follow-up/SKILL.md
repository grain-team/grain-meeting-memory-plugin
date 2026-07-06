---
name: follow-up
description: Draft sendable work product from Grain meetings — a follow-up email, client recap, internal update, brief, decision log, evidence pack, or ticket. Use when the user wants to send, post, or file anything based on what happened in meetings.
argument-hint: "<what to draft, from which meeting(s), for whom>"
---

# Follow-Up

Turn meetings into something **sendable**. This is the plugin's anchor skill — the output goes to real people, so the bar is highest here.

Read first:
- `${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` — audience inference, draft-first, per-type best practices, the residue ban, delivery
- `${CLAUDE_PLUGIN_ROOT}/references/retrieval.md` — if the source meetings aren't already identified
- `${CLAUDE_PLUGIN_ROOT}/references/evidence.md` — citing claims inside artifacts

## Workflow

1. **Identify the source meetings.** "The call this morning" → `list_attended_meetings` for today; a topic or account → scope per the retrieval playbook. Notes and action items first; transcript only where exact wording matters. Done when every meeting the artifact draws on is identified and its notes are read.
2. **Infer audience and form**, per the artifact playbook: draft first with assumptions stated.
3. **Draft free, then check.** One clean pass from the evidence. Done when every commitment, owner, and date in the draft matches the record — verified against `fetch_meeting_action_items`, not notes prose — and the residue ban passes.
4. **Deliver** per the playbook's delivery rules.

## Specific to this skill

- External audiences: no Grain links unless the user confirms they're shareable; no internal candor.
- Multi-meeting artifacts state their coverage ("covers the three Acme calls since June 10").
