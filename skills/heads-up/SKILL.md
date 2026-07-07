---
name: heads-up
description: Give the user a heads-up from Grain meeting history when their work names a specific person, company, account, or project — even though they didn't ask about meetings. Use when an email, doc, or draft being written or edited mentions a client or account, when the user weighs a should-we decision about a customer, or when they cite what a specific person wants, said, or agreed to. Skip purely personal or social messages (birthday notes, congratulations, small talk) even when they name someone.
argument-hint: ""
---

# Heads-Up

The user is doing other work that names a person, company, or account. Grain may know something **material** about them. Check quietly; give a heads-up only if it changes what the user is doing.

This skill is an experiment in Grain as ambient organizational memory. Its failure mode is noise — err hard toward silence.

Read if surfacing anything: `${CLAUDE_PLUGIN_ROOT}/references/evidence.md`.

## Rules

1. **Check cheaply and silently.** Whether Grain knows the entity is discovered here, not assumed: `search_companies` / `search_persons` first — unknown entity means you're done, silently. Known entity: recent notes or one targeted `search_in_transcripts` on the specific matter. No deep sweeps — this is a side-check, never the main task, and gets abandoned if slow. If Grain tools are missing or the connector is unauthorized, stand down silently — never interrupt unrelated work with a connect prompt (that's the retrieval playbook's job, for skills the user invoked on purpose).
2. **The materiality bar.** A heads-up is warranted only for what would change the user's action:
   - They're about to contradict or forget a commitment
   - The counterpart already stated a position on exactly this
   - A decision they're relitigating was already made, with rationale
   - A date, number, or claim they're using differs from what was said

   "There have been some meetings about this" is never material. Background is never material.
3. **The heads-up itself: brief, cited, then out of the way.** One to three sentences, each with meeting/date/link, set apart from the main work — then continue the task.
4. **Silence is the default outcome.** Nothing material → say nothing about Grain at all, including that you checked.
5. **Never act on the record unasked** — this skill reads; it creates and tags nothing.
