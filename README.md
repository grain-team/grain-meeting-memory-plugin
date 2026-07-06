# Meeting Memory by Grain

Claude that remembers your meetings. Turn Grain recordings into answers you can trust, follow-ups you can send, and prep you can walk in with — cited back to the source meeting, every time.

**Status: internal dogfood.** Not published or submitted. Feedback via PRs to this repo.

## What you can say

No commands to learn — just talk about your work:

- *"Write the follow-up email for my Acme call this morning."*
- *"What did the customer say about pricing last month?"*
- *"Did she actually agree to the September date?"*
- *"Where are we with the Meridian renewal?"*
- *"What did I miss last week?"*
- *"What are my open action items?"*
- *"Prep me for my 2pm with Jordan."*
- *"What keeps coming up in our sales calls?"*

Claude will also quietly check Grain when you're drafting something about a customer or account it knows — and only speak up if it finds something that changes what you're doing.

## What makes it different

- **Evidence, always.** Answers cite the meeting, date, speaker, and link. "I couldn't find that in the record" is an answer you'll actually get.
- **Work product, not summaries.** Follow-ups, updates, recaps, and briefs shaped for the person receiving them — clean enough to send without editing, with no AI residue.
- **Cross-meeting memory.** State, commitments, and patterns folded across all your conversations — the thing no single meeting summary can do.

## Requirements

A [Grain](https://grain.com) account. Nothing else — the Grain MCP connector is bundled (`.mcp.json`, pointed at `https://api.grain.com/_/mcp`) and you'll authenticate on first use. Slack, Linear, calendar, and CRM connectors are never required.

## Install

**Claude Code:**

```
/plugin marketplace add <this-repo-github-url>
/plugin install meeting-memory-by-grain@grain
```

**Claude (org/workspace):** Settings → Plugins → sync from this GitHub repo.

**Local development:**

```
claude --plugin-dir /path/to/grain-meeting-memory-plugin
```

## Dogfooding

Use it on real work, not demos. When something is great or wrong, capture: your prompt, whether the right skill fired, whether it found the right meetings, whether you trusted the output without re-checking, and whether an artifact was sendable as-is. Then open a PR or an issue. Repeated failures matter more than one-offs.

Test prompts per skill: [docs/test-prompts.md](docs/test-prompts.md).
Design, decision log, and dogfood protocol: [DESIGN.md](DESIGN.md).
Editing skill descriptions? Run the routing regression first: `python3 evals/run-triggers.py`.

## Privacy

The plugin reads your Grain workspace through Grain's MCP server with your own credentials — it sees exactly what you can see in Grain, nothing more. It never creates clips, tags meetings, or writes to any system without your explicit confirmation.
