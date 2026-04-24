#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    'README.md',
    'CLAUDE.md',
    'EXAMPLES.md',
    '.claude-plugin/plugin.json',
    '.claude-plugin/marketplace.json',
]


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


for rel in REQUIRED_FILES:
    path = ROOT / rel
    if not path.exists():
        fail(f'missing required file: {rel}')

for rel in ['.claude-plugin/plugin.json', '.claude-plugin/marketplace.json']:
    path = ROOT / rel
    with path.open('r', encoding='utf-8') as fh:
        json.load(fh)

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for needle in ['CLAUDE.md', 'EXAMPLES.md', '.claude-plugin/plugin.json']:
    if needle not in readme:
        fail(f'README.md is missing expected reference: {needle}')

print('validation_ok')
