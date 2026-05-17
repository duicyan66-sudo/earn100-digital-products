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
    out=[]
    out.append(f"# Repository context pack\n\nRoot: `{root}`\n\n## Git\n```text\n{git_info(root)}\n```\n")
    out.append('## Language/file mix\n'+'\n'.join(f"- {k}: {v}" for k,v in lang.most_common())+'\n')
    out.append(f"## File tree sample\n```text\n{tree}\n```\n")
    out.append('## TODO / FIXME markers\n'+('\n'.join(todos[:80]) if todos else 'No TODO/FIXME markers found.')+'\n')
    out.append('## Selected file snippets\n')
    for rel,sample in snippets:
        out.append(f"### `{rel}`\n```\n{sample}\n```\n")
    pathlib.Path(args.out).write_text('\n'.join(out), encoding='utf-8')
    print(f"Wrote {args.out} with {len(files)} files indexed")
if __name__=='__main__': main()
