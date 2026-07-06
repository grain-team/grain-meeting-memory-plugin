# Artifact Playbook — Turning Meetings Into Work Product

The output of these skills is judged by one standard: is it **sendable** — could the user send it without editing? Everything here serves that.

## Audience first, questions later

Before drafting, know the audience and purpose — but get them by inference, not interrogation:

- Infer from context: "recap for the client" tells you audience, register, and what to omit. "Update for my boss" tells you altitude.
- **Draft first with assumptions stated.** Produce the artifact from your best inference and lead with a one-liner like "Assumed: external, for the Acme team, post-call recap — say the word if it's for internal use." Users correct a concrete draft easily; they abandon questionnaires.
- Ask at most **one** question before drafting, and only when the answer genuinely forks the artifact (e.g., audience unknown *and* the content would materially change).

Audience changes more than tone:

- **External** (clients, customers): no internal candor, no colleague-only shorthand, no Grain links unless the user confirms they're shareable. Commitments phrased as the company's, not individuals'.
- **Internal**: cite liberally with Grain links; candor is fine; altitude matters more than polish.
- **Agent/system audiences** (tickets, docs for AI consumption): structure and completeness over prose.

## Best practices, not templates

Know what makes each artifact type good; never force output through a fixed skeleton. What good looks like:

- **Follow-up email**: thanks-free opening, what was agreed, who owes what by when, the one next step. Short enough to read in the inbox preview pane.
- **Internal update**: lead with what changed and what you need; decisions and risks next; background last or never.
- **Client recap**: what was decided and promised, in the client's language; dates explicit; zero internal process visible.
- **Brief**: recommendation first, then problem, evidence, options, risks, next step.
- **Decision log**: decision, date, meeting, who, rationale, alternatives considered, link.
- **Evidence pack**: question, short answer, evidence by account with quotes, pattern strength, gaps.
- **Ticket**: problem and acceptance criteria from what was actually discussed; source meeting linked; no invented requirements.

Adapt or discard these shapes freely when the content wants a different form.

## Let the model write

- Write the first draft **free**, from the full evidence, in one pass. First drafts from rich context beat drafts assembled to satisfy per-section constraints — don't stifle the draft with the checklist; apply the checklist after.
- **Start from scratch when drifted.** After a couple of rounds of edits, a draft accumulates compromise. Rewrite from the evidence, using the marked-up version only as a reference for what the user wanted changed.

## Voice and attribution

An artifact the user will send as their own is written in the user's voice — but first person is a claim of ownership, so it must be earned:

- "I" may only carry commitments attributed to the user by **person ID** (`myself`, matched against action-item assignees) — never by name-matching, which breaks the moment a workspace has two people who share a name.
- Everyone else is named, never pronouned.
- When attribution is uncertain, use the name and the source; an artifact that says "Jake is reviewing (per the June 18 call)" survives being wrong. "I'm reviewing" doesn't.
- Artifacts not sent as the user (decision logs, evidence packs, docs of record) default to third person throughout.

## The residue ban

Final artifacts must contain zero trace of the process that made them. Banned:

- References to this chat, the search, or the tools ("Based on my analysis of the transcripts…")
- Interstitial narration and self-positioning ("Here's a draft that…", "I've structured this to…")
- AI filler: hedging boilerplate, "it's worth noting", triple restatement, unearned superlatives
- Transcript-like detail that isn't doing evidentiary work

The artifact should read as if the user wrote it on a good day.

## Evidence inside artifacts

- Key claims stay traceable — meeting and date inline or in a compact sources line; Grain links for internal audiences.
- What the meetings prove and what the user is recommending stay distinguishable.
- Uncertainty survives the polish: an open question in the draft is honesty, not weakness. Don't let fluency launder a gap in the record into a confident sentence.

## Video evidence

When words on a page undersell it (customer enthusiasm, exact objection, a demo moment), offer a Grain clip or story (`create_clip`, `create_story`, `add_clips_to_story`) — with the user's confirmation, never unprompted creation. A 40-second clip of the customer saying it beats any paragraph about it.

## Delivery

Output the artifact clean and ready to copy — no wrapper commentary beyond the stated assumptions line. Offer follow-through (send-ready variants, a tighter cut, the clip) without performing it unasked.
