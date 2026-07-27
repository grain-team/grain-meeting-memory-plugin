# Contributing

## Dogfooding

Use it on real work, not demos. When something is great or wrong, capture: your prompt, whether the right skill fired, whether it found the right meetings, whether you trusted the output without re-checking, and whether an artifact was sendable as-is. Then open a PR or an issue. Repeated failures matter more than one-offs.

Test prompts per skill: [docs/test-prompts.md](docs/test-prompts.md).
Design, decision log, and dogfood protocol: [DESIGN.md](DESIGN.md).
Editing skill descriptions? Run the routing regression first: `python3 evals/run-triggers.py`.
