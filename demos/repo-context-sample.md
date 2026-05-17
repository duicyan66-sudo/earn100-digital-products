# Repository context pack

Root: `/root/earn100-github-pages`

## Git
```text
Branch: main
HEAD: 7d91e13
Dirty files:
clean
```

## Language/file mix
- Markdown: 15
- YAML: 5
- Python: 2
- JavaScript: 1
- JSON: 1

## File tree sample
```text
script.js
README.md
products.json
CHANGELOG.md
docs/positioning.md
docs/agent-debugging.md
docs/repo-context-engineering.md
docs/prompt-regression.md
docs/github-launch-playbook.md
prompts/senior-code-review-agent.md
prompts/agent-debugging-playbook.md
.github/ISSUE_TEMPLATE/product-request.yml
.github/ISSUE_TEMPLATE/agent-failure.yml
.github/ISSUE_TEMPLATE/config.yml
.github/DISCUSSION_TEMPLATE/show-and-tell.md
tools/repo_context_pack.py
tools/prompt_regression.py
pro-preview/README.md
samples/free-sample.md
marketing/launch-plan.md
marketing/objection-handling.md
marketing/posts.md
examples/prompt-cases.yml
workflows/agent-quality-gate.yml
```

## TODO / FIXME markers
- `tools/repo_context_pack.py:7` language stats, important files, TODO/FIXME markers, and selected snippets.
- `tools/repo_context_pack.py:75` if re.search(r'\b(TODO|FIXME|HACK|XXX)\b', line, re.I):
- `tools/repo_context_pack.py:85` out.append('## TODO / FIXME markers\n'+('\n'.join(todos[:80]) if todos else 'No TODO/FIXME markers found.')+'\n')

## Selected file snippets

### `script.js`
```
const dict={
zh:{nav_free:"免费工具",nav_products:"付费产品",nav_github:"GitHub 运营",nav_delivery:"交付",nav_payment:"付款",eyebrow:"给 GitHub 开发者的 coding agent 工具包",hero_title:"别把整个仓库乱塞给 AI。把上下文、审查和回归测试做成工程流程。",hero_copy:"这里有可运行的免费脚本，也有给资深开发者的付费包。它们不卖玄学，卖的是更少的误改、更快的审查、更稳的 agent 工作流。",cta_products:"看付费产品",cta_github:"打开 GitHub 仓库",stat_paid:"个付费包",stat_tools:"个免费 CLI 工具",stat_price:"低价起步，先跑通销售",free_label:"free layer",free_title:"先给 GitHub 用户一点真东西。",free_copy:"免费层必须能运行。否则开发者不会信后面的付费包。",free_card1_title:"仓库上下文打包",free_card1_copy:"把代码、约束和忽略规则整理成 agent 更容易读的 brief，减少“看错文件”的概率。",free_card2_title:"提示词回归检查",free_card2_copy:"用 YAML 维护失败用例，改 prompt 前后都能跑一遍，不靠感觉判断变好了没有。",products_label:"paid packs",products_title:"面向 GitHub 用户和技术大牛的 5 个付费产品。",products_copy:"产品故意做小。一个包解决一个工程化问题，买家拿到后当天能用。",download_zip:"下载加密包",p1:"给日常使用 coding agent 的开发者：整理仓库上下文、审查输出、做提示词回归。",p2:"给资深工程师的代码审查包：不看“像不像对”，只追风险、边界和可回滚性。",p3:"给会折腾 agent 的技术用户：定位跑偏、循环、误改、测试假绿和上下文污染。",p4:"给真正关心上下文质量的人：把仓库、约束、任务和验证路径打包给 agent。",p5:"给写提示词和 agent workflow 的人：别凭感觉改 prompt，用用例和检查表卡住退化。",github_label:"GitHub native marketing",github_title:"宣传也放在 GitHub 里做。",github_copy:"README 负责解释价值，Issues 负责收集需求，docs 负责承接搜索，release notes 负责让仓库看起来像一个在维护的项目。",gh1_title:"README 当落地页",gh1_copy:"第一页就说清楚免费工具、付费包、价格和交付方式。",gh2_title:"Issue 模板当需求入口",gh2_copy:"让用户提交“想要什么包”和“agent 卡在哪里”。这比硬广自然。",gh3_title:"docs 做长尾搜索",gh3_copy:"围绕 repo context、agent debugging、prompt regression 写短文，吸引真正懂的人。",buy_label:"delivery",buy_title:"购买方式很简单，但不假装全自动。",buy_copy:"GitHub Pages 是静态网站，不能核验付款。国内用户可以扫码付款；海外用户请先联系 Telegram：@xi_yh_bot 获取 PayPal、Wise 或其他可用收款方式。付款后发送产品代码和截图，确认后发密码。",payment_caption:"国内用户扫码付款；海外用户联系 Telegram",footer_preview:"付费包预览",footer_contact:"交付说明",footer_payment:"付款方式"},
en:{nav_free:"Free tools",nav_products:"Paid packs",nav_github:"GitHub marketing",nav_delivery:"Delivery",nav_payment:"Payment",eyebrow:"Coding agent workflow kits for GitHub developers",hero_title:"Stop dumping your repo into AI. Turn context, review, and regression into an engineering loop.",hero_copy:"This repo has runnable free tools and paid packs for people who already use coding agents. No magic claims. Just fewer bad edits, tighter reviews, and cleaner agent handoffs.",cta_products:"View paid packs",cta_github:"Open GitHub repo",stat_paid:"paid packs",stat_tools:"free CLI tools",stat_price:"starter price, built to sell first",free_label:"free layer",free_title:"Give GitHub users something real first.",free_copy:"The free layer has to run. Developers will not trust a paid pack if the repo is only a brochure.",free_card1_title:"Repo context packing",free_card1_copy:"Package code, constraints, and ignore rules into a cleaner brief so the agent is less likely to stare at the wrong files.",free_card2_title:"Prompt regression checks",free_card2_copy:"Keep failure cases in YAML and run them before and after prompt changes. Do not judge prompts by vibes.",products_label:"paid packs",products_title:"Five paid products for GitHub users and senior technical buyers.",products_copy:"Each pack is intentionally small. One pack, one engineering problem, usable the same day.",download_zip:"Download encrypted zip",p1:"For developers using coding agents every day: repo context, agent review, and prompt regression in one pack.",p2:"For senior engineers reviewing risky diffs: boundaries, rollback, security notes, and PR comments that do not waste time.",p3:"For people debugging agent loops, wrong edits, fake green tests, and polluted context.",p4:"For engineers who care about what goes into the model before code comes out.",p5:"For teams maintaining prompts and agent workflows. Change prompts with cases, not gut feel.",github_label:"GitHub native marketing",github_title:"Marketing lives on GitHub too.",github_copy:"README explains the value. Issues collect demand. Docs catch search traffic. Release notes make the repo feel maintained because it is.",gh1_title:"README as landing page",gh1_copy:"The first screen shows free tools, paid packs, prices, and delivery.",gh2_title:"Issues as demand capture",gh2_copy:"Users can ask for packs and describe where their agents fail. That feels better than hard selling.",gh3_title:"Docs for long-tail search",gh3_copy:"Short pages around repo context, agent debugging, and prompt regression attract the right technical readers.",buy_label:"delivery",buy_title:"Simple purchase flow. No fake automation.",buy_copy:"GitHub Pages is static, so it cannot verify payment. If you can use the QR code, use it. If not, message @xi_yh_bot on Telegram for PayPal, Wise, or another available payment method. Send the product code and payment screenshot after payment.",payment_caption:"QR for China. International buyers: message Telegram first.",footer_preview:"Paid pack preview",footer_contact:"Delivery notes",footer_payment:"Payment"}
};
const btn=document.getElementById('langToggle');
function setLang(lang){document.documentElement.lang=lang==='zh'?'zh-CN':'en';document.querySelectorAll('[data-i18n]').forEach(el=>{const key=el.dataset.i18n;if(dict[lang][key])el.textContent=dict[lang][key]});btn.textContent=lang==='zh'?'EN':'中文';localStorage.setItem('ai-devops-lang',lang)}
btn.addEventListener('click',()=>setLang((localStorage.getItem('ai-devops-lang')||'zh')==='zh'?'en':'zh'));
setLang(localStorage.getItem('ai-devops-lang')||'en');
```

### `README.md`
```
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
| AI-DEVOPS-PRO | AI DevOps Pro Pack | $4.9 / ¥29.9 | developers using coding agents |
| CR-AGENT-PRO | Code Review Agent Pro | $5.9 / ¥39.9 | senior reviewers |
| AGENT-DEBUG-PRO | Agent Debugging War Room | $6.9 / ¥49.9 | agent-heavy teams |
| CONTEXT-ENGINEERING-PRO | Repo Context Engineering Pro | $8.9 / ¥59.9 | staff engineers and tool builders |
| PROMPT-REGRESSION-PRO | Prompt Regression Test Suite | $9.9 / ¥69.9 | prompt/workflow maintainers |

Payment and delivery: download the encrypted zip, then pay. If you can use the QR code on the site, use it. If you are outside China, message Telegram `@xi_yh_bot` for PayPal, Wise, or another available payment method. After payment, send the product code and receipt/screenshot. The password is sent after confirmation.

## Run the free tools

```bash
python tools/repo_context_pack.py --root . --out repo-context.md
python tools/prompt_regression.py examples/prompt-cases.yml --out prompt-report.md
```

## GitHub launch notes

This repository is the storefront, the proof, and the support desk. Use Issues for questions and product requests. The paid packs are small, practical, and meant to save time on real agent workflows, not to impress anyone with buzzwords.
```

### `products.json`
```
[
  {
    "code": "AI-DEVOPS-PRO",
    "name_en": "AI DevOps Pro Pack",
    "name_zh": "AI DevOps Pro Pack",
    "price": "$4.9 / ¥29.9",
    "audience": "developers",
    "line_en": "A working kit for repo context, agent review, and prompt regression.",
    "line_zh": "给日常使用 coding agent 的开发者：整理仓库上下文、审查输出、做提示词回归。",
    "zip": "downloads/AI-DEVOPS-PRO_paid_encrypted.zip"
  },
  {
    "code": "CR-AGENT-PRO",
    "name_en": "Code Review Agent Pro",
    "name_zh": "Code Review Agent Pro",
    "price": "$5.9 / ¥39.9",
    "audience": "senior",
    "line_en": "A stricter review system for senior engineers who do not trust pretty diffs.",
    "line_zh": "给资深工程师的代码审查包：不看“像不像对”，只追风险、边界和可回滚性。",
    "zip": "downloads/CR-AGENT-PRO_paid_encrypted.zip"
  },
  {
    "code": "AGENT-DEBUG-PRO",
    "name_en": "Agent Debugging War Room",
    "name_zh": "Agent Debugging War Room",
    "price": "$6.9 / ¥49.9",
    "audience": "senior",
    "line_en": "For teams debugging Claude Code, Codex, Cursor, OpenCode, and weird agent loops.",
    "line_zh": "给会折腾 agent 的技术用户：定位跑偏、循环、误改、测试假绿和上下文污染。",
    "zip": "downloads/AGENT-DEBUG-PRO_paid_encrypted.zip"
  },
  {
    "code": "CONTEXT-ENGINEERING-PRO",
    "name_en": "Repo Context Engineering Pro",
    "name_zh": "Repo Context Engineering Pro",
    "price": "$8.9 / ¥59.9",
    "audience": "senior",
    "line_en": "A context design kit for people who care what goes into the model before code comes out.",
    "line_zh": "给真正关心上下文质量的人：把仓库、约束、任务和验证路径打包给 agent。",
    "zip": "downloads/CONTEXT-ENGINEERING-PRO_paid_encrypted.zip"
  },
  {
    "code": "PROMPT-REGRESSION-PRO",
    "name_en": "Prompt Regression Test Suite",
    "name_zh": "Prompt Regression Test Suite",
    "price": "$9.9 / ¥69.9",
    "audience": "developers",
    "line_en": "A lightweight way to stop prompt changes from silently making agents worse.",
    "line_zh": "给写提示词和 agent workflow 的人：别凭感觉改 prompt，用用例和检查表卡住退化。",
    "zip": "downloads/PROMPT-REGRESSION-PRO_paid_encrypted.zip"
  }
]
```

### `CHANGELOG.md`
```
# Changelog

## 2026-05-17

- Added four new paid packs for code review, agent debugging, repo context engineering, and prompt regression.
- Rebuilt the landing page with a Chinese/English language switch.
- Added GitHub issue templates for product requests and agent failure reports.
- Added docs that support GitHub search and repo-native marketing.
```

### `docs/positioning.md`
```
# Product positioning

This repository is no longer a generic prompt pack. It is positioned as a small, practical **AI developer operations kit** for people building with coding agents.

## Who it is for

- Solo builders using Claude Code, Codex, Cursor, OpenCode, or local agents
- Maintainers who need better context packs for LLM reviews
- Teams starting to review prompts like code
- Developers who want reusable debugging and review playbooks

## What is free

- `tools/repo_context_pack.py`: creates an LLM-ready repository context pack
- `tools/prompt_regression.py`: creates prompt regression review checklists
- `prompts/*`: senior review and agent debugging prompts
- `workflows/agent-quality-gate.yml`: GitHub Actions starter workflow

## What is paid

The Pro Pack is for people who want the complete operating system: deeper checklists, more review prompts, reusable issue templates, agent evaluation matrices, launch copy, and private playbooks.

## What not to claim

- Do not promise income.
- Do not claim the tools replace senior engineers.
- Do not claim automated payment verification; GitHub Pages is static.
```

### `docs/agent-debugging.md`
```
# Agent debugging

When an agent fails, do not immediately ask it to fix the fix. First find the first wrong assumption. Was the wrong file selected? Was a tool result partial? Did a test pass because it mocked the bug away?

The fastest recovery is usually smaller context, one failing command, and a prompt that asks for diagnosis before edits.
```

### `docs/repo-context-engineering.md`
```
# Repo context engineering

Bad agent output often starts with bad context. Too many files confuse the model. Too few files make it invent glue. The trick is to package the part of the repo that controls behavior, then add constraints and tests.

A good context brief answers five questions: what should change, what must not change, which files decide behavior, which tests prove it, and what a rollback would look like.
```

### `docs/prompt-regression.md`
```
# Prompt regression

Prompts change like code, but most teams do not test them like code. Keep a few cases that represent failures you never want back: missed constraints, unsafe broad rewrites, ignored tests, or fake confidence.

A tiny YAML file and a review checklist are enough to start. You can add heavier evals later if the workflow earns it.
```

### `docs/github-launch-playbook.md`
```
# GitHub launch playbook

This launch should happen inside the repo first. Do not start with cold spam. Make the project look useful when someone lands here from search or a comment.

## What to do on GitHub

1. Keep the README short and blunt. Developers scan.
2. Use Issues for product requests and bug reports.
3. Publish small docs around repo context, agent debugging, and prompt regression.
4. Add release notes when a paid pack changes.
5. Answer questions in public when the answer helps future buyers.

## Good GitHub comments

Mention the repo only when someone is already discussing coding agents, repo context, prompt evals, or AI code review. Lead with the free tool. The paid pack can wait.
```

### `prompts/senior-code-review-agent.md`
```
# Senior code review agent prompt

Use this when you want an LLM to review a pull request like a careful staff engineer, not like a style nit bot.

```text
You are reviewing a pull request for production readiness.

Review order:
1. Summarize what changed in plain language.
2. Identify behavior changes, not just file changes.
3. Look for data loss, auth, payment, privacy, concurrency, migration, and rollback risks.
4. Check whether tests cover the changed behavior.
5. Separate blocking issues from optional improvements.
6. If something is uncertain, say what evidence would resolve it.

Output:
- Verdict: approve / request changes / needs clarification
- Blocking issues
- Non-blocking improvements
- Missing tests
- Questions

Do not invent facts. Quote file paths and function names when possible.
```
```

### `prompts/agent-debugging-playbook.md`
```
# Agent debugging playbook

A practical prompt for debugging flaky AI-agent workflows.

```text
You are debugging an AI agent failure. Do not patch first.

Phase 1: Reconstruct
- What was the user trying to accomplish?
- What tools/actions were actually used?
- Where did observed behavior diverge from expected behavior?

Phase 2: Localize
- Is this model reasoning, tool schema, auth, environment, state, network, or UI?
- What is the smallest reproduction?

Phase 3: Fix
- Propose the smallest change that addresses the root cause.
- Identify any side effects.

Phase 4: Verify
- Give exact commands/tests.
- State what output would prove the fix worked.
```
```

### `.github/ISSUE_TEMPLATE/product-request.yml`
```
name: Paid pack request
description: Suggest a new AI DevOps Kit paid pack
title: "Pack request: "
labels: ["product-request"]
body:
  - type: textarea
    id: problem
    attributes:
      label: What agent workflow keeps hurting?
      description: Describe the repeated failure, not the dream feature.
    validations:
      required: true
  - type: textarea
    id: current
    attributes:
      label: What do you use now?
      description: Prompts, scripts, review habits, docs, anything.
  - type: input
    id: buyer
    attributes:
      label: Who would pay for this?
      placeholder: solo dev, senior reviewer, infra team, prompt maintainer
```

### `.github/ISSUE_TEMPLATE/agent-failure.yml`
```
name: Agent failure report
description: Share a coding agent failure this repo should help prevent
title: "Agent failure: "
labels: ["agent-failure"]
body:
  - type: textarea
    id: failure
    attributes:
      label: What went wrong?
      description: Keep it concrete. Wrong file, wrong test, wrong assumption, bad review, loop, etc.
    validations:
      required: true
  - type: textarea
    id: proof
    attributes:
      label: What proved it was wrong?
      description: Test output, review note, production symptom, or a smaller reproduction.
```

### `.github/ISSUE_TEMPLATE/config.yml`
```
blank_issues_enabled: true
```

### `.github/DISCUSSION_TEMPLATE/show-and-tell.md`
```
# Show an agent workflow

What did you automate? What still needed human review? What broke?

If you mention a paid pack, keep it honest. Say what it helped with and what it did not solve.
```

### `tools/repo_context_pack.py`
```
#!/usr/bin/env python3
"""Create a compact, LLM-ready repository context pack.

Why this exists:
  Senior devs do not want to paste random files into chat. This script walks a
  repo, filters noise, and emits a single Markdown context pack with tree,
  language stats, important files, TODO/FIXME markers, and selected snippets.

Usage:
  python tools/repo_context_pack.py --root . --out repo-context.md
  python tools/repo_context_pack.py --root ~/project --max-file-kb 80 --include py,ts,tsx,md
"""
from __future__ import annotations
import argparse, os, pathlib, re, subprocess, textwrap
from collections import Counter

DEFAULT_EXCLUDES = {
    '.git', 'node_modules', '.venv', 'venv', '__pycache__', 'dist', 'build',
    '.next', '.turbo', '.cache', 'coverage', '.pytest_cache', 'target',
}
IMPORTANT = {'README.md','AGENTS.md','CLAUDE.md','package.json','pyproject.toml','requirements.txt','Dockerfile','docker-compose.yml','Makefile'}
EXT_LANG = {'.py':'Python','.js':'JavaScript','.ts':'TypeScript','.tsx':'TSX','.jsx':'JSX','.go':'Go','.rs':'Rust','.java':'Java','.md':'Markdown','.yml':'YAML','.yaml':'YAML','.json':'JSON','.sh':'Shell'}

def should_skip(path: pathlib.Path) -> bool:
    return any(part in DEFAULT_EXCLUDES for part in path.parts) or path.is_symlink()

def safe_read(path: pathlib.Path, max_bytes: int) -> str | None:
    try:
        data = path.read_bytes()
    except Exception:
        return None
    if b'\x00' in data or len(data) > max_bytes:
        return None
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return data.decode('utf-8', errors='replace')

def git_info(root: pathlib.Path) -> str:
    def run(cmd):
        try:
            return subprocess.check_output(cmd, cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
        except Exception:
            return ''
    branch = run(['git','branch','--show-current'])
    head = run(['git','rev-parse','--short','HEAD'])
    status = run(['git','status','--short'])
    return f"Branch: {branch or 'n/a'}\nHEAD: {head or 'n/a'}\nDirty files:\n{status or 'clean'}"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--out', default='repo-context.md')
    ap.add_argument('--max-file-kb', type=int, default=64)
    ap.add_argument('--include', default='py,js,ts,tsx,jsx,go,rs,java,md,yml,yaml,json,sh')
    args=ap.parse_args()
    root=pathlib.Path(args.root).expanduser().resolve()
    include={'.'+x.strip().lstrip('.') for x in args.include.split(',') if x.strip()}
    max_bytes=args.max_file_kb*1024
    files=[]
    for p in root.rglob('*'):
        rel=p.relative_to(root)
        if should_skip(rel) or not p.is_file():
            continue
        if p.name in IMPORTANT or p.suffix in include:
            files.append(p)
    lang=Counter(EXT_LANG.get(p.suffix, p.suffix or 'other') for p in files)
    todos=[]
    snippets=[]
    for p in files:
        txt=safe_read(p, max_bytes)
        if txt is None: continue
        rel=str(p.relative_to(root))
        for i,line in enumerate(txt.splitlines(),1):
            if re.search(r'\b(TODO|FIXME|HACK|XXX)\b', line, re.I):
                todos.append(f"- `{rel}:{i}` {line.strip()[:180]}")
        if p.name in IMPORTANT or len(snippets)<18:
            sample='\n'.join(txt.splitlines()[:80])
            snippets.append((rel, sample))
    tree='\n'.join(str(p.relative_to(root)) for p in files[:260])
```

### `tools/prompt_regression.py`
```
#!/usr/bin/env python3
"""Tiny prompt regression runner for agent/prompt changes.

It does not call any model. Instead, it gives you a repeatable checklist file
for expected behavior so prompt changes can be reviewed like code.

Usage:
  python tools/prompt_regression.py examples/prompt-cases.yml --out prompt-report.md
"""
from __future__ import annotations
import argparse, json, re, sys, pathlib
try:
    import yaml
except Exception:
    yaml=None

def load(path):
    text=pathlib.Path(path).read_text(encoding='utf-8')
    if path.endswith('.json'):
        return json.loads(text)
    if yaml:
        return yaml.safe_load(text)
    # minimal YAML-ish fallback for the included example
    cases=[]; cur=None
    for line in text.splitlines():
        if line.startswith('- name:'):
            if cur: cases.append(cur)
            cur={'name':line.split(':',1)[1].strip().strip('"')}
        elif cur and ':' in line:
            k,v=line.strip().split(':',1); cur[k]=v.strip().strip('"')
    if cur: cases.append(cur)
    return {'cases':cases}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('cases'); ap.add_argument('--out', default='prompt-report.md')
    args=ap.parse_args(); data=load(args.cases)
    lines=['# Prompt regression checklist','']
    for i,c in enumerate(data.get('cases',[]),1):
        lines += [f"## {i}. {c.get('name','Unnamed')}", '', '**Input**', '```text', c.get('input',''), '```', '', '**Expected properties**']
        for e in c.get('expect',[]) if isinstance(c.get('expect'), list) else [c.get('expect','')]:
            lines.append(f"- [ ] {e}")
        lines += ['', '**Failure modes to watch**']
        for f in c.get('avoid',[]) if isinstance(c.get('avoid'), list) else [c.get('avoid','')]:
            lines.append(f"- [ ] Does not: {f}")
        lines.append('')
    pathlib.Path(args.out).write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote {args.out}")
if __name__=='__main__': main()
```

### `pro-preview/README.md`
```
# Paid packs preview

These are paid packs. The zip files are public, but encrypted. After payment, send the product code and payment screenshot to Telegram `@xi_yh_bot`.


## AI-DEVOPS-PRO · AI DevOps Pro Pack · ¥29.9

A working kit for repo context, agent review, and prompt regression.

中文：给日常使用 coding agent 的开发者：整理仓库上下文、审查输出、做提示词回归。

Download: `downloads/AI-DEVOPS-PRO_paid_encrypted.zip`


## CR-AGENT-PRO · Code Review Agent Pro · ¥39.9

A stricter review system for senior engineers who do not trust pretty diffs.

中文：给资深工程师的代码审查包：不看“像不像对”，只追风险、边界和可回滚性。

Download: `downloads/CR-AGENT-PRO_paid_encrypted.zip`


## AGENT-DEBUG-PRO · Agent Debugging War Room · ¥49.9

For teams debugging Claude Code, Codex, Cursor, OpenCode, and weird agent loops.

中文：给会折腾 agent 的技术用户：定位跑偏、循环、误改、测试假绿和上下文污染。

Download: `downloads/AGENT-DEBUG-PRO_paid_encrypted.zip`


## CONTEXT-ENGINEERING-PRO · Repo Context Engineering Pro · ¥59.9

A context design kit for people who care what goes into the model before code comes out.

中文：给真正关心上下文质量的人：把仓库、约束、任务和验证路径打包给 agent。

Download: `downloads/CONTEXT-ENGINEERING-PRO_paid_encrypted.zip`


## PROMPT-REGRESSION-PRO · Prompt Regression Test Suite · ¥69.9

A lightweight way to stop prompt changes from silently making agents worse.

中文：给写提示词和 agent workflow 的人：别凭感觉改 prompt，用用例和检查表卡住退化。

Download: `downloads/PROMPT-REGRESSION-PRO_paid_encrypted.zip`
```
