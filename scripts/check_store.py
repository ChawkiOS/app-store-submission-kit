#!/usr/bin/env python3
"""Checks a STORE.md file: character limits and Apple keywords.

Usage: python3 check_store.py STORE.md

Each field is written like this in STORE.md (bold title with its limit, then the text as a quote):

    **App Store subtitle** (30 characters max):

    > The hot potato with friends

The limit is read from the parentheses ("30 characters max", "4,000 characters max", "100 caractères max").
For a text spanning several quote lines, the lines are joined with line breaks,
and Markdown bold (**…**) is removed, as in the console.
Keywords (a field whose title contains "keywords" or "mots-clés") are also checked:
commas without spaces, no duplicates, no word from the name or subtitle of the same section.
"""
import re
import sys
import unicodedata

TITLE = re.compile(r'^\*\*(.+?)\*\*\s*\(([^)]*?)(\d[\d\s.,  ]*)\s*(?:charac|caract)[^)]*\)', re.I)


def clean(text: str) -> str:
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    return unicodedata.normalize('NFC', text)


def read_fields(lines):
    fields = []
    section = ''
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('## '):
            section = line[3:].strip()
        m = TITLE.match(line.strip())
        if m:
            name = m.group(1).strip()
            limit = int(re.sub(r'\D', '', m.group(3)))
            j = i + 1
            while j < len(lines) and not lines[j].startswith('>'):
                if lines[j].startswith('**') or lines[j].startswith('#'):
                    break
                j += 1
            block = []
            while j < len(lines) and lines[j].startswith('>'):
                block.append(lines[j][1:].removeprefix(' '))
                j += 1
            text = clean('\n'.join(block).strip())
            # Value written on the same line: "**Name** (30 characters max): PATATE".
            inline = line.strip()[m.end():].split(':', 1)
            if not text and len(inline) == 2 and inline[1].strip():
                text = clean(inline[1].strip())
            fields.append({'section': section, 'name': name, 'limit': limit, 'text': text, 'line': i + 1})
            i = j
            continue
        i += 1
    return fields


def check_keywords(field, fields):
    problems = []
    text = field['text']
    if ', ' in text:
        problems.append('space after a comma (Apple counts every space)')
    keywords = [k.strip() for k in text.split(',') if k.strip()]
    seen = set()
    for keyword in keywords:
        key = keyword.lower()
        if key in seen:
            problems.append(f'duplicate: "{keyword}"')
        seen.add(key)
    # Words already indexed by Apple: name and subtitle of the same section.
    indexed = set()
    for other in fields:
        if other['section'] == field['section'] and re.search(r'\b(name|nom|subtitle|sous-titre)\b', other['name'], re.I):
            indexed.update(w.lower() for w in re.findall(r'\w+', other['text']))
    for keyword in keywords:
        for word in re.findall(r'\w+', keyword):
            if word.lower() in indexed and len(word) > 2:
                problems.append(f'"{word}" is already in the name or subtitle (useless in the keywords)')
    return problems


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    lines = open(sys.argv[1], encoding='utf-8').read().split('\n')
    fields = read_fields(lines)
    if not fields:
        sys.exit('No "**Title** (N characters max)" field found.')
    errors = 0
    for field in fields:
        length = len(field['text'])
        status = 'ok' if 0 < length <= field['limit'] else ('EMPTY' if length == 0 else 'TOO LONG')
        if status != 'ok':
            errors += 1
        print(f"{status:9} {length:5}/{field['limit']:<5} {field['section'][:18]:18} {field['name']} (line {field['line']})")
        if re.search(r'keyword|mots-cl|palabras clave|palavras-chave|schlüsselw|parole chiave', field['name'], re.I):
            for p in check_keywords(field, fields):
                errors += 1
                print(f'          keywords: {p}')
    print('\nEverything is within limits.' if errors == 0 else f'\n{errors} problem(s) to fix.')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
