#!/usr/bin/env python3
"""Controleer alle skills in deze repo.

Fouten (laten de controle mislukken):
  - map zonder SKILL.md, of SKILL.md zonder geldige frontmatter
  - `name` wijkt af van de mapnaam, `description` ontbreekt of is te lang
  - Markdown-link naar een bestand binnen de repo dat niet bestaat
  - ongeldige JSON in evals/
  - iets dat op een geheime sleutel lijkt
  - met --public: telefoonnummers, of e-mailadressen bij persoonlijke maildiensten
    of .nl-domeinen, buiten licentiebestanden

Waarschuwingen (alleen gemeld):
  - SKILL.md langer dan 500 regels
  - beschrijving zegt niet wanneer de skill gebruikt wordt
  - `references/...`-pad dat in geen enkele skill bestaat

Gebruik: python3 scripts/check_skills.py [--public]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"licenses", "scripts"}
TEXT_EXT = {".md", ".py", ".js", ".ts", ".json", ".yaml", ".yml", ".html", ".sh", ".txt", ".csv"}
FILE_LINK = re.compile(r"\]\(([^)\s#]+?\.[A-Za-z0-9]{1,5})(?:#[^)]*)?\)")
SECRETS = re.compile(
    r"(?<![A-Za-z0-9-])sk-(?:ant-[a-z0-9]+-|proj-)?[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,}|xox[abpr]-[A-Za-z0-9-]{10,}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----|AIza[0-9A-Za-z_-]{35}"
)
PHONE = re.compile(r"(?<!\d)(?:\+31[ -]?6|06)[ -]?\d{8}(?!\d)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]*[A-Za-z]{2,}")
# Alleen persoonlijke maildiensten en .nl-domeinen; voorbeeldadressen (press@yourcompany.com) mogen.
EMAIL_PRIVATE = re.compile(r"@(gmail|googlemail|outlook|hotmail|live|icloud|me|yahoo|ziggo|kpnmail|planet|home|xs4all|hetnet|casema)\.[a-z.]+$|\.nl$", re.I)

errors, warnings = [], []


def rel(p):
    return os.path.relpath(p, ROOT)


def frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    fm = m.group(1)
    fields = {}
    for key in ("name", "description"):
        f = re.search(rf"^{key}:[ \t]*(.*?)(?=^\S[^:\n]*:|\Z)", fm, re.M | re.S)
        if f:
            v = f.group(1).strip()
            if v[:1] in (">", "|"):
                v = v[1:].strip()
            fields[key] = " ".join(v.strip("\"'").split())
    return fields


def text_files(base):
    for d, dirs, files in os.walk(base):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for f in files:
            if os.path.splitext(f)[1].lower() in TEXT_EXT:
                yield os.path.join(d, f)


def main():
    public = "--public" in sys.argv
    skills = sorted(
        d for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d)) and not d.startswith(".") and d not in SKIP_DIRS
    )
    all_refs = set()
    for s in skills:
        for d, _, files in os.walk(os.path.join(ROOT, s)):
            for f in files:
                all_refs.add(os.path.relpath(os.path.join(d, f), os.path.join(ROOT, s)).replace(os.sep, "/"))

    for s in skills:
        path = os.path.join(ROOT, s, "SKILL.md")
        if not os.path.isfile(path):
            errors.append(f"{s}/: geen SKILL.md")
            continue
        text = open(path, encoding="utf-8").read()
        fm = frontmatter(text)
        if fm is None:
            errors.append(f"{s}/SKILL.md: geen geldige frontmatter (--- ... ---)")
            continue
        if fm.get("name") != s:
            errors.append(f"{s}/SKILL.md: name is '{fm.get('name')}', verwacht '{s}'")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{s}/SKILL.md: description ontbreekt")
        elif len(desc) > 1024:
            errors.append(f"{s}/SKILL.md: description is {len(desc)} tekens (max 1024)")
        elif not re.search(r"\b(use|used|when|trigger|gebruik|wanneer)\b", desc, re.I) and "disable-model-invocation: true" not in text:
            warnings.append(f"{s}/SKILL.md: beschrijving zegt niet wanneer de skill gebruikt wordt")
        lines = text.count("\n") + 1
        if lines > 500:
            warnings.append(f"{s}/SKILL.md: {lines} regels (richtlijn: max 500)")

        for f in text_files(os.path.join(ROOT, s)):
            if f.endswith(".json") and "/evals/" in f.replace(os.sep, "/"):
                try:
                    json.load(open(f, encoding="utf-8"))
                except ValueError as e:
                    errors.append(f"{rel(f)}: ongeldige JSON ({e})")
            if not f.endswith(".md"):
                continue
            body = open(f, encoding="utf-8").read()
            for target in FILE_LINK.findall(body):
                if re.match(r"^[a-z]+:", target) or target.startswith("/"):
                    continue
                full = os.path.normpath(os.path.join(os.path.dirname(f), target))
                if not full.startswith(ROOT):
                    continue
                if not os.path.exists(full):
                    errors.append(f"{rel(f)}: link naar '{target}' bestaat niet")
            for ref in set(re.findall(r"`((?:references|assets|scripts)/[\w./-]+\.\w+)`", body)):
                if ref not in all_refs:
                    warnings.append(f"{rel(f)}: '{ref}' bestaat in geen enkele skill")

    for f in text_files(ROOT):
        r = rel(f).replace(os.sep, "/")
        if r.startswith("scripts/"):
            continue
        body = open(f, encoding="utf-8", errors="replace").read()
        if SECRETS.search(body):
            errors.append(f"{r}: bevat iets dat op een geheime sleutel lijkt")
        if public and not r.startswith("licenses/") and not re.search(r"(LICENSE|OFL)[^/]*$", r):
            if PHONE.search(body):
                errors.append(f"{r}: bevat een telefoonnummer (openbare repo)")
            for e in set(EMAIL.findall(body)):
                if EMAIL_PRIVATE.search(e):
                    errors.append(f"{r}: bevat e-mailadres {e} (openbare repo)")

    for w in warnings:
        print(f"::warning::{w}" if os.environ.get("GITHUB_ACTIONS") else f"waarschuwing: {w}")
    for e in errors:
        print(f"::error::{e}" if os.environ.get("GITHUB_ACTIONS") else f"FOUT: {e}")
    print(f"\n{len(skills)} skills gecontroleerd: {len(errors)} fouten, {len(warnings)} waarschuwingen")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
