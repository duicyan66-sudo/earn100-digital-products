# AI DevOps Kit

Small tools and paid workflow packs for developers who use coding agents in real repositories.

[Live site](https://duicyan66-sudo.github.io/earn100-digital-products/) · [Payment notes](https://duicyan66-sudo.github.io/earn100-digital-products/payment.html) · [Demo context output](demos/repo-context-sample.md) · [Demo prompt report](demos/prompt-report-sample.md)

Coding agents are useful, but they fail in boring ways: missing the right file, trusting a pretty diff, looping on a bad instruction, or making a prompt change that fixes one case and breaks three others.

This repo gives away the basic workflow. The paid packs are for people who want the checklists, rubrics, and playbooks already packaged.

中文：这是一个面向 GitHub 开发者的 AI 工程化工具包。免费部分可以直接 fork 和运行。付费包放在 `downloads/`，zip 已加密，付款后通过 Telegram 获取密码。

## Try the free layer

```bash
python tools/repo_context_pack.py --root . --out repo-context.md
python tools/prompt_regression.py examples/prompt-cases.yml --out prompt-report.md
```

What you get for free:

- `tools/repo_context_pack.py`: turns a repo into a cleaner context brief for coding agents.
- `tools/prompt_regression.py`: turns prompt cases into a review report.
- `examples/prompt-cases.yml`: sample prompt regression cases.
- `prompts/`: starter prompts for code review and agent debugging.
- `workflows/agent-quality-gate.yml`: a GitHub Actions starter workflow.

## Paid packs

| code | pack | price | for |
|---|---:|---:|---|
| AI-DEVOPS-PRO | AI DevOps Pro Pack | $4.9 / ¥29.9 | developers using coding agents |
| CR-AGENT-PRO | Code Review Agent Pro | $5.9 / ¥39.9 | senior reviewers |
| AGENT-DEBUG-PRO | Agent Debugging War Room | $6.9 / ¥49.9 | agent-heavy teams |
| CONTEXT-ENGINEERING-PRO | Repo Context Engineering Pro | $8.9 / ¥59.9 | staff engineers and tool builders |
| PROMPT-REGRESSION-PRO | Prompt Regression Test Suite | $9.9 / ¥69.9 | prompt and workflow maintainers |

Each paid zip is encrypted. For `AI-DEVOPS-PRO`, international buyers can pay directly with PayPal: https://www.paypal.com/ncp/payment/QXZK7CPVEXCHL. After payment, send the product code and receipt to [@xi_yh_bot](https://t.me/xi_yh_bot). The unzip password is sent after confirmation.

For the other packs, message [@xi_yh_bot](https://t.me/xi_yh_bot) for PayPal, Wise, or another available payment method. China buyers can use the QR code on the site if their payment app supports it.

## Why this exists

Most agent workflows are still copy-paste rituals. Someone drops half a repo into chat, asks for a review, then tries to remember which prompt worked last time.

This project makes that process a little more explicit:

- package repo context before asking for edits;
- review agent output against risk, rollback, and test evidence;
- keep prompt cases in a file instead of in your head;
- write down failure modes when an agent goes sideways.

## Good first issues

Use Issues if you want one of these:

- a new prompt regression case;
- a repo-context rule for a language or framework;
- a stricter code-review checklist;
- a paid pack focused on your workflow.

The repo is small on purpose. If something here feels overbuilt, open an issue and say where it gets in the way.
