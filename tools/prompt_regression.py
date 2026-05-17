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
