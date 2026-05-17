# AI DevOps Kit

Small tools and paid packs for developers who use coding agents seriously.

The free repo gives you working scripts, prompts, workflow files, and examples. The paid packs go deeper: code review, agent debugging, repo context design, and prompt regression.

中文：这是一个面向 GitHub 开发者的 AI 工程化工具包。免费部分可以直接 fork 和运行。付费包放在 `downloads/`，zip 已加密，付款后通过 Telegram 获取密码。

## Free tools

- `tools/repo_context_pack.py` packages a repo into a cleaner context file for coding agents.
- `tools/prompt_regression.py` turns prompt cases into a review report.

## Paid packs

| code | pack | price | for |
|---|---:|---:|---|
| AI-DEVOPS-PRO | AI DevOps Pro Pack | ¥29.9 | developers using coding agents |
| CR-AGENT-PRO | Code Review Agent Pro | ¥39.9 | senior reviewers |
| AGENT-DEBUG-PRO | Agent Debugging War Room | ¥49.9 | agent-heavy teams |
| CONTEXT-ENGINEERING-PRO | Repo Context Engineering Pro | ¥59.9 | staff engineers and tool builders |
| PROMPT-REGRESSION-PRO | Prompt Regression Test Suite | ¥69.9 | prompt/workflow maintainers |

Payment and delivery: download the encrypted zip, pay from the site, then send the product code and payment screenshot to Telegram `@xi_yh_bot`.

## Run the free tools

```bash
python tools/repo_context_pack.py --root . --out repo-context.md
python tools/prompt_regression.py examples/prompt-cases.yml --out prompt-report.md
```

## GitHub launch notes

This repository is the storefront, the proof, and the support desk. Use Issues for questions and product requests. The paid packs are small, practical, and meant to save time on real agent workflows, not to impress anyone with buzzwords.
