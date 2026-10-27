# Meeting Memory by Grain

An AI assistant that remembers your meetings. Turn Grain recordings into answers you can trust, follow-ups you can send, and prep you can walk in with — cited back to the source meeting, every time.

Works in Claude (Claude Code, claude.ai, desktop), Cursor, Grok Bot, and Grok Build from this one repository.

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

## What makes it different

- **Evidence, always.** Answers cite the meeting, date, speaker, and link. "I couldn't find that in the record" is an answer you'll actually get.
- **Work product, not summaries.** Follow-ups, updates, recaps, and briefs shaped for the person receiving them — clean enough to send without editing, with no AI residue.
- **Cross-meeting memory.** State, commitments, and patterns folded across all your conversations — the thing no single meeting summary can do.
- **Speaks up when it matters.** Quietly checks Grain when you're drafting something about a customer or account it knows — and only interrupts if it finds something that changes what you're doing.

## Requirements

A [Grain](https://grain.com) account (the free plan is enough). Nothing else — the Grain MCP server is bundled (`.mcp.json`, pointed at `https://api.grain.com/_/mcp`) and you'll sign in with your Grain account on first use. Slack, Linear, calendar, and CRM connectors are never required.

## Install

**Claude Code:**

```
/plugin marketplace add grain-team/grain-meeting-memory-plugin
/plugin install meeting-memory-by-grain@grain
```

**Claude (org/workspace):** Settings → Plugins → sync from this GitHub repo.

**Cursor:** Marketplace → search "Grain" → Install. Sign in to Grain when prompted.

**Grok Bot:** Connect apps → search "Grain" → Install. Sign in to Grain when prompted.

**Grok Build:**

```
grok plugin install grain-team/grain-meeting-memory-plugin --trust
```

Then `/mcp` and sign in to grain.

**Local development:**

```
claude --plugin-dir /path/to/grain-meeting-memory-plugin
grok plugin install /path/to/grain-meeting-memory-plugin --trust
```

For Cursor, copy or symlink the repo into `~/.cursor/plugins/local/`.

## How the repo is laid out

One set of skills and one MCP config serve every client. Each client reads only its own manifest:

| Client | Manifest | MCP config | Skills |
|---|---|---|---|
| Claude Code, claude.ai | `.claude-plugin/plugin.json` | `.mcp.json` | all of `skills/` |
| Cursor, Grok Bot | `.cursor-plugin/plugin.json` | `.mcp.json` (via `mcpServers`) | all of `skills/` |
| Grok Build | `.claude-plugin/plugin.json` (accepted natively) | `.mcp.json` | all of `skills/` |

Skills reference the shared playbooks in `references/` by path relative to the plugin root, so they read the same way in every client.

## Network and credentials

The plugin makes requests to exactly one endpoint, Grain's hosted MCP server at `https://api.grain.com/_/mcp`, over HTTPS. Authentication is OAuth 2.1 with PKCE and dynamic client registration, discovered from the server's `.well-known` metadata; no API keys, secrets, or environment variables are shipped or required. The plugin contains no hooks, scripts, or binaries.

## Privacy

The plugin reads your Grain workspace through Grain's MCP server with your own credentials — it sees exactly what you can see in Grain, nothing more. It never creates clips, tags meetings, or writes to any system without your explicit confirmation.

## Testing

Per-skill test prompts live in [docs/test-prompts.md](docs/test-prompts.md). To verify an install: ask *"What was my last meeting?"* — the first call should trigger the Grain sign-in, and the answer should name a real meeting with a link.
