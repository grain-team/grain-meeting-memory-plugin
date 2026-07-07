# Retrieval Playbook — How To Research Grain Meetings Well

The difference between a naive answer and a trusted one is usually retrieval, not reasoning. Follow this sequence.

## 0. If Grain isn't connected

An unauthenticated connector is not a dead end — never answer with "authorize it in settings, then ask me again."

- **Attempt one cheap call anyway** (`myself`). claude.ai and Claude Code intercept the unauthenticated call and surface the connect/authorize prompt inline — attempting the call is what triggers the auth flow. Do not assume the session can't run it.
- If no Grain tools exist in the session at all, the connector isn't enabled: give the exact path (claude.ai: Settings → Connectors → Grain → Connect; Claude Code: `/mcp`), then hold the user's question and run it in this same conversation the moment they say they're connected.

## 1. Resolve entities before searching

Names in the user's request are ambiguous until resolved:

- `myself` — who the user is (workspace ID, person ID). Needed for "my meetings", "what do I owe".
- `search_persons` — resolve "Sarah" to a person ID before filtering by her.
- `search_companies` — resolve "Acme" to a company before pulling account history.
- `list_workspace_users` — distinguish internal colleagues from external participants.

Default scoping is **account/person-first**: when a request could scope by account, person, or topic, prefer the account or person — that's the unit of memory for most Grain users.

## 2. Scope the meeting set

- `list_meetings` / `list_attended_meetings` with filters (participants, time window) — establish which meetings are even relevant before reading anything.
- Note the count — cross-meeting claims need a denominator ("across 6 Acme calls since May").

Default time windows when unspecified: 7 days for catch-up/follow-up sweeps, 90 days for account questions, all-time only for explicit "have we ever" questions.

## 3. Read the cheap layers first

In cost order:

1. **Meeting metadata** (`fetch_meeting`) — title, date, participants. Often enough to rank relevance.
2. **AI notes** (`fetch_meeting_notes`) — the main synthesis layer. Most questions are answerable here.
3. **Action items** (`fetch_meeting_action_items`) — structured commitments with assignee, due date, status, transcript URL.
4. **User's private notes** (`fetch_user_recording_notes`) — what the user themselves flagged.
5. **Targeted transcript search** (`search_in_transcripts`) — hybrid semantic + keyword across meetings. The workhorse for "what was said about X".
6. **Full transcript** (`fetch_meeting_transcript`) — last resort; only when exact wording, sequence, or tone matters, and only for meetings already known to be relevant.

Never open with full-transcript fetches across many meetings. It is slow, floods context, and produces worse synthesis than notes-first reading.

## 4. Search like a researcher, not a keyword matcher

- Run `search_in_transcripts` with the user's phrasing **and** synonyms/adjacent language ("pricing" → "cost", "budget", "quote", "discount").
- When verifying a claim, also search for **counter-evidence** — what would be true if the claim were false.
- When a hit looks right, read enough surrounding context to confirm the meaning wasn't clipped mid-thought.
- Attribute before you count: five mentions in one call is one data point. Count distinct meetings and distinct accounts/people.
- Note who raised each point — a theme our own team keeps introducing is a different finding than one customers bring up unprompted.

## 5. Enrichment tools (use when present, never require)

- `get_dossier_for_company` — assembled account context in one call; the first stop for any account or customer question before manual searching.
- `fetch_collection` / `list_collections` — curated meeting groups; great scope when the user names a project or initiative.
- `list_smart_topics` — workspace-tracked topics; check before building a pattern answer from scratch.
- `fetch_deal` / `list_open_deals` — HubSpot-linked deal context for account questions (may be unavailable; degrade silently).
- `list_coaching_feedback` / `fetch_meeting_coaching_feedback` — sales coaching context (same).
- `list_clips`, `list_stories`, `fetch_story` — existing curated evidence worth checking before rebuilding it.

## 6. Links are part of retrieval

Call `resolve_urls` for every meeting (and clip/collection/story) you intend to cite. Action items often carry their own transcript URLs — use them for timestamp-level citations.

## 7. Latency discipline

Speed is a feature of trust:

- Get to the first useful output fast; state the scope you chose and offer to widen — a narrow answer delivered now beats a broad one delivered late.
- Cap initial sweeps (roughly 10–15 meetings of notes); disclosure of what a capped sweep skipped is governed by the evidence playbook's coverage honesty.
- Stop when the answer has converged. More retrieval after convergence adds latency, not accuracy.

## 8. When retrieval comes up empty

Empty is a finding. Report what was searched (scope, window, terms), state plainly that nothing was found, and offer the most promising next search (wider window, different phrasing, other participants). Never pad an empty result into a plausible-sounding answer.
