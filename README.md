# AI DevOps Kit

A practical AI developer operations kit for coding-agent workflows.

This repo is the free edition. It contains runnable utilities and prompts for developers using Claude Code, Codex, Cursor, OpenCode, or other coding agents in real repositories.

## Free tools

- `tools/repo_context_pack.py` — generate an LLM-ready repository context pack
- `tools/prompt_regression.py` — turn prompt behavior cases into a review checklist
- `prompts/senior-code-review-agent.md` — staff-engineer style code review prompt
- `prompts/agent-debugging-playbook.md` — debug failed agent runs systematically
- `workflows/agent-quality-gate.yml` — GitHub Actions starter workflow

## Quick start

```bash
python tools/repo_context_pack.py --root . --out repo-context.md
python tools/prompt_regression.py examples/prompt-cases.yml --out prompt-report.md
```

## Pro Pack

The Pro Pack contains deeper review prompts, agent failure playbooks, prompt regression cases, launch copy, and operating checklists.

Landing page: https://duicyan66-sudo.github.io/earn100-digital-products/

Contact after payment: https://t.me/xi_yh_bot

## Philosophy

Coding agents are useful, but only when the workflow around them is disciplined: context in, constraints in, review out, verification before claims. This kit is designed around that loop.
