# Quickstart for coding agents

This repo is meant to be tried before it is bought.

## 1. Pack the repository context

```bash
python tools/repo_context_pack.py --root . --out repo-context.md
```

Use the generated file as the first message or attachment for Claude Code, Codex, Cursor, OpenCode, or another coding agent. The goal is simple: give the agent the files, constraints, and structure it needs without dumping random noise into the context window.

## 2. Run a prompt regression pass

```bash
python tools/prompt_regression.py examples/prompt-cases.yml --out prompt-report.md
```

The report is not a benchmark. It is a review checklist. It helps you notice when a prompt change fixes one case and quietly breaks another.

## 3. Where the paid packs fit

The free tools prove the workflow. The paid packs add templates, rubrics, review sheets, and failure playbooks for people who want the workflow already written down.

- `AI-DEVOPS-PRO`: starter workflow for solo developers.
- `CR-AGENT-PRO`: stricter code review prompts and PR checklists.
- `AGENT-DEBUG-PRO`: triage notes for agent loops, context drift, fake green tests, and bad edits.
- `CONTEXT-ENGINEERING-PRO`: file-selection rules and token-budget worksheets.
- `PROMPT-REGRESSION-PRO`: larger prompt case libraries and release checklists.

No magic. Just less rework.
