# Meeting Memory by Grain — Design & Working Doc

Team-facing. This repo stays private through dogfood; the public release will be a fresh single-commit snapshot, so write freely here (rules of the road at the bottom).

**Status (July 6, 2026):** built, validated against production with real meeting data, 15/15 on the trigger-routing regression. Next: initial commit → push → team dogfood → submission decision this week. Origin story: the [June 29 exec sync](https://grain.com/note/dc4e2ff8-976c-4fb6-b7bb-9c2a26539d3a/Oew9af5aSI2F0bz7lHsxFn8jrkKp6h1EbLHM697Z) (also `internal/` on Jake's machine, with the full agent-context handoff doc).

## Premise

Anyone can already connect the Grain MCP server to Claude. The plugin's entire value is the delta between **Claude with raw Grain tools** and **Claude doing excellent meeting-grounded work**. And since Grain's own app already does per-meeting summaries, notes, and action items, the plugin only wins where Claude adds what the app structurally can't:

- **Cross-meeting synthesis** — answers and state folded across many conversations.
- **Audience-shaped drafting** — work product composed for a reader, not a recap.
- **Presence inside the user's other work** — meeting memory arriving where the work is happening.

That delta is three competencies, encoded once as shared playbooks:

1. **Retrieval craft** (`references/retrieval.md`) — resolve people/companies first, search synonyms, establish denominators, prefer notes over transcripts until exact wording matters, narrow-then-widen, know when to stop.
2. **Evidence discipline** (`references/evidence.md`) — every claim traces to a meeting/date/link; "not found" is a valid answer; fact, interpretation, and recommendation stay separate; confidence marked; conflicts surfaced.
3. **Artifact craft** (`references/artifacts.md`) — audience-first; best practices per artifact type, not templates; free first draft; start-from-scratch when drifted; zero chat residue.

## Who it's for

The average Grain user: meeting-heavy, customer-facing, not AI-fluent — CS, sales, founders, PMs, agencies, recruiters. Three constraints follow:

- **No concepts to learn.** Every skill is reachable by a sentence they already say.
- **Lifecycle mental model.** Before the meeting / after the meeting / between meetings.
- **Draft first, ask later.** Infer aggressively, state assumptions, invite correction. At most one clarifying question, only when the answer genuinely changes the output.

## Usage bets (where value concentrates)

The dogfood week exists to test this table. Investment is deliberately uneven:

| Tier | Capability | Why |
| --- | --- | --- |
| 1 | Drafting from meetings (follow-ups, recaps, updates) | Daily moment; output gets *sent*; beats native summaries on audience, multi-meeting, and context |
| 1 | Mid-work record questions ("what did we promise Acme?") | High frequency for customer-facing users; high-stakes moments win or lose trust permanently |
| 2 | Where-things-stand / catch-up | Real but episodic; slowest operation — defaults narrow and fast |
| 2 | What-do-I-owe | Weekly; value is cross-meeting aggregation, dedup, staleness — not re-listing action items |
| 3 | Prep | Overrated in every meeting-AI roadmap including ours; kept lean, delights when it fires |
| 3 | Patterns / voice-of-customer | Narrow persona, quarterly; a mode of `what-did-we-say`, not a skill |
| ? | Heads-up (ambient) | The dark horse: zero behavior change required; dogfood decides |

If the week is all drafting and record questions, that's the submission story; the rest stays as description-level surface.

## V1 skill set

| Moment | Skill | The sentence that summons it |
| --- | --- | --- |
| Before | `prep-me` | "Prep me for my call with Acme" |
| After | `follow-up` | "Write the follow-up email" / "Turn this into an update" / "Recap for the client" |
| Between | `what-do-i-owe` | "What are my action items?" / "What did I promise?" |
| Between | `where-things-stand` | "Where are we with Acme?" / "Catch me up" / "What did I miss?" |
| Anytime | `what-did-we-say` | "What did we say about pricing?" / "Did she actually agree to that?" / "What keeps coming up?" |
| Invisible | `heads-up` | None — checks Grain when your work names a person, account, or project; speaks only if material |

Seams:

- `what-did-we-say` absorbs source-finding, claim verification (per-claim verdicts: supported / contradicted / not found), and pattern questions (denominator discipline). Same trigger context, correctness standard, and output shape.
- `follow-up` is the anchor and golden path: follow-up email is the front door; updates, briefs, decision logs, evidence packs, tickets, and clips/stories are output modes of the same skill.
- `heads-up` is the differentiated experiment: consult the record unprompted, strict materiality bar, silence by default. Cut without ceremony if noisy.
- Deferred to V2: document-level claim audit ("audit this PRD against the record"), interaction-general dossiers, a deterministic hook variant of heads-up if it under-fires.

## Design rules

- **Grain-only.** No other connector required, ever. Companions (Slack, Linear, calendar, CRM) may enrich later versions.
- **Natural invocation first.** Descriptions written so skills fire from ordinary work language; slash commands are a fallback, not the model.
- **Draft first.** Best-inference output with assumptions stated; never interrogate before value.
- **Account/person-first scoping.** Grain's base is customer-facing; their unit of memory is the account.
- **Speed is a feature of trust.** Narrow-and-stated beats broad-and-slow; deep sweeps offer to widen.
- **Every output links back into Grain.** The link is the trust mechanism and the loop into the product.
- **Read-only by default.** No clips/stories/collections/tags/external writes without explicit confirmation.
- **Honest failure.** Thin evidence or empty windows → plain statement + suggested next search, never padding.

## What V1 is not

- Not role-specific (horizontal; no "for sales" variants).
- Not a knowledge-graph or local-memory system.
- Not dependent on optional Grain features (deals, coaching, collections, dossiers enrich when present; nothing requires them).

## Decision log

So we don't re-litigate:

- **July 1 — hybrid architecture.** Thin intent-shaped skills over three shared playbooks. Rejected: six self-contained skills (70% duplicated content); 2-skill competency shape (too little trigger surface).
- **July 1 — six lifecycle skills, filtered for the average user.** Patterns demoted to a mode of `what-did-we-say` (no distinct trigger/output shape). Claim-audit and dossier deferred to V2; their cheap forms live inside `what-did-we-say` and `prep-me`.
- **July 2 — skill-authoring pass** (Matt Pocock's writing-great-skills framework): one trigger per branch, single source of truth between skills and playbooks, checkable completion criteria, leading words (*sendable*, *the record*, *ledger*, *fold*, *materiality bar*). Cut always-on cost 729 → ~535 tokens with zero routing regressions.
- **July 6 — `ambient-recall` renamed `heads-up`.** Trigger rewritten to be evaluable from the message alone (the old "known person" wording required information the model can't have pre-check). Personal/social exclusion added after the eval suite caught an over-trigger on "birthday message for my coworker."
- **July 6 — kept 6 skills.** Considered merging `prep-me` into `where-things-stand` for a tighter story; Jake called keep.

## Validation so far (July 6, live against production)

- **Production parity:** prod exposes 43 tools vs the June 22 local reference's 35. Breaking rename caught and fixed: projects → **collections**. New tools adopted: `get_dossier_for_company` (now prep's first stop for accounts), `list_smart_topics`. Reference doc in `~/Work/grain/projects/plugins/` updated.
- **Golden path (follow-up):** 58s end-to-end on a real call. Cheap-layers retrieval, stated assumptions, working Grain link, owner-grouped action items verified against the structured tool, and an unprompted staleness flag ("this call was 2.5 weeks ago — some items may be done").
- **Trust anchor (what-did-we-say):** given a deliberately mis-framed question ("did we decide to build our own plugin *rather than* pursue Anthropic placement?"), it corrected the premise — both paths in tandem — with speaker-attributed quotes, links, and two earlier meetings surfaced from Grain search. 147s. (Caveat: the June 29 transcript was in the working dir, so quote sourcing was partially local; team dogfood is the clean test of citation quality.)
- **Trigger routing:** 15/15 (`evals/trigger-cases.json`). Notables: entity buried in *pasted* content fires `heads-up`; "Jordan said she wants X, plan around it" fires `heads-up` (the quiet-verify moment); customer-facing *drafting* correctly routes to `follow-up` instead.

## Dogfood protocol

1. Install: `/plugin marketplace add grain-team/<repo>` then `/plugin install meeting-memory-by-grain@grain` (Claude Code), or org settings → Plugins → sync from GitHub / zip upload (claude.ai). On claude.ai, enable the Grain connector if the bundled MCP config isn't honored.
2. Use it on real work, not demos — prompts to start from: `docs/test-prompts.md`.
3. Capture per use: the prompt · right skill fired? · right meetings found? · trusted without re-checking? · artifact sendable as-is?
4. Feedback as PRs where possible; repeated failures matter more than one-offs. Any description edit must pass `python3 evals/run-triggers.py` (15 cases, ~2 min).
5. The week must answer two things: **which tiers matched real usage**, and **does `heads-up` earn its place**.

## Publication rules of the road

- This repo is private; the public release will be a **fresh single-commit snapshot** to a new repo at submission time. So: commit and comment candidly here — none of it ships.
- `internal/` is gitignored and never committed anywhere (exec transcripts, strategy docs).
- This file gets swapped for its scrubbed public version at snapshot time (already drafted: `internal/DESIGN-public-draft.md`).

## Open questions

- Does `heads-up` over- or under-trigger in sustained real usage?
- Which Grain link formats are shareable outside a workspace? (Affects citations in external-facing artifacts.)
- Final public naming ("Meeting Memory by Grain" is the working name).
- claude.ai org-plugin surface: is the bundled `.mcp.json` honored, or does the workspace Grain connector carry the tools?
