---
name: what-did-we-say
description: Answer from the Grain meeting record with cited evidence. Use when the user asks what was said or decided and why, whether someone actually said or agreed to something, or what keeps coming up across meetings.
argument-hint: "<question, claim to verify, or theme>"
---

# What Did We Say

Answer from the record, with evidence the user can click. This skill gets asked in high-stakes moments ("the customer says we promised X — did we?"); one invented answer ends the plugin's credibility.

Read first:
- `${CLAUDE_PLUGIN_ROOT}/references/retrieval.md` — entity resolution, synonym and counter-evidence search, cheap-layers-first
- `${CLAUDE_PLUGIN_ROOT}/references/evidence.md` — citation rules, verification verdicts, pattern denominators, "not found"

## Modes

**Lookup** — "what did we say about pricing?" Search, then:

```text
Short answer.

Evidence:
- "[quote or marked paraphrase]" — speaker, meeting, date, link
- ...

My read: (only if interpretation is needed)
```

**Verification** — "did she actually agree to that?" Per-claim verdicts per the evidence playbook. Done when every claim in question has a verdict: supported, contradicted, or not found.

**Patterns** — "what keeps coming up?" Denominators and strength grading per the evidence playbook. "Looks like a one-off so far" is a good answer.
