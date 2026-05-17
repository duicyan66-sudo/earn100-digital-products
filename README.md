# AI DevOps Kit

Small tools and paid workflow packs for developers who use coding agents in real repositories.

[Live site](https://duicyan66-sudo.github.io/earn100-digital-products/) · [PayPal checkout](https://www.paypal.com/ncp/payment/QXZK7CPVEXCHL) · [After payment](https://duicyan66-sudo.github.io/earn100-digital-products/payment-success.html) · [Order guide](https://duicyan66-sudo.github.io/earn100-digital-products/docs/order-guide.md)

Coding agents fail in boring ways: they miss the right file, trust a pretty diff, loop on a bad instruction, or make a prompt change that fixes one case and breaks three others.

This repo gives away the basic workflow. The paid pack is for people who want the checklists, rubrics, and playbooks already packaged.

中文：这是一个面向 GitHub 开发者的 AI 工程化工具包。免费部分可以直接 fork 和运行。`AI-DEVOPS-PRO` 已有 PayPal 付款链接；付费 zip 已加密，付款后通过邮箱获取密码。

## Fast purchase

Current smooth checkout path:

1. Buy `AI-DEVOPS-PRO` with PayPal: https://www.paypal.com/ncp/payment/QXZK7CPVEXCHL
2. Download the encrypted ZIP: `downloads/AI-DEVOPS-PRO_paid_encrypted.zip`
3. Email PayPal receipt + product code `AI-DEVOPS-PRO` to qq466886@126.com
4. Receive the ZIP password after confirmation, usually within 12 hours.

Other packs are available by manual request until each has a separate PayPal link. This avoids wrong-product payments.

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

- `AI-DEVOPS-PRO` — AI DevOps Pro Pack — $4.90 — direct PayPal checkout available.
- `CR-AGENT-PRO` — Code Review Agent Pro — $5.90 — request payment link on email.
- `AGENT-DEBUG-PRO` — Agent Debugging War Room — $6.90 — request payment link on email.
- `CONTEXT-ENGINEERING-PRO` — Repo Context Engineering Pro — $8.90 — request payment link on email.
- `PROMPT-REGRESSION-PRO` — Prompt Regression Test Suite — $9.90 — request payment link on email.

## Why this exists

Most agent workflows are still copy-paste rituals. Someone drops half a repo into chat, asks for a review, then tries to remember which prompt worked last time.

This project makes that process more explicit:

- package repo context before asking for edits;
- review agent output against risk, rollback, and test evidence;
- keep prompt cases in a file instead of in your head;
- write down failure modes when an agent goes sideways.

## Buyer safety

Do not send passwords, seed phrases, private keys, payment passwords, identity documents, or PayPal login details. A product code and payment receipt are enough.
