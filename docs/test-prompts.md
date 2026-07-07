# Dogfood Test Prompts

Real-work prompts per skill. Use your own accounts/names. For each run, note: did the right skill fire, did it find the right meetings, did you trust it without re-checking, was an artifact sendable as-is.

## follow-up (the golden path)

- "Write the follow-up email for my [account] call this morning."
- "Turn the last three [account] meetings into a status update for [manager]."
- "Draft a recap of yesterday's product sync I can post in Slack."
- "Make a decision log entry for the pricing decision from Monday's leadership meeting."

## what-did-we-say (the trust anchor)

- "What did [customer] say about pricing in the last couple months?"
- "Did [person] actually commit to the September date?"
- "Why did we decide to [decision]? Who pushed for it?"
- "What keeps coming up as a blocker in our sales calls?"
- Ask about something you know is NOT in any meeting — it should say "not found," not improvise.

## where-things-stand

- "Where are we with [account]?"
- "Catch me up on [project] — I've been out all week."
- "What's the latest on [topic]? Last I heard we were doing X." (Test supersession: was X reversed since?)

## what-do-i-owe

- "What are my open action items from this week?"
- "What did people promise me that I haven't gotten?"
- "Anything still open between me and [person] before our 1:1?"

## prep-me

- "Prep me for my call with [person] tomorrow."
- "Brief me on [account] before the renewal conversation."
- "What should I not step on in the [team] meeting?"

## heads-up (the experiment — don't invoke it, just work)

- Think through a decision out loud that a recorded meeting already settled ("should we offer [account] a discount?") — does it tell you what was already decided?
- Ask for a proofread/edit of your own writing that mentions a known account — does it check Grain and only speak up if material?
- Work on something involving an account Grain doesn't know — does it stay appropriately silent?
- Note: asking to *draft* something customer-facing may route to `follow-up` instead — that's correct; follow-up does full retrieval plus artifact craft.

## First-run / disconnected (run once per surface)

- With the Grain connector disconnected (or before first auth), ask any skill prompt above — does the connect/authorize prompt appear inline, or at minimum an exact click-path (claude.ai: Settings → Connectors → Grain; Claude Code: `/mcp`)? "Authorize it and ask me again" is a fail.
- After connecting, does it pick the original question back up in the same conversation without you re-asking?

## Cross-cutting checks

- Are Grain links present and correct? Click two per session.
- Is scope stated ("last 30 days, 8 meetings") on synthesized answers?
- Vague prompt test: "catch me up" with no scope — does it pick a sensible scope and say so, rather than interrogating you?
- Speed: how long to first useful output on a broad question?
