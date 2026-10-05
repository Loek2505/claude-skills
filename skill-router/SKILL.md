---
name: skill-router
description: Recommends which installed skills fit the current project and prompt, including manual-only skills (ponytail, prototype, pick-ui-library, review-animations) that Claude cannot trigger by itself. Use when starting a coding, UI/animation, marketing or Swift task in a session, when starting work in a new project, or when the user asks which skills to use.
---

# Skill router

Goal: at the start of a task, tell the user in at most 3 lines which skills fit, and especially which **manual-only** skills they should switch on, because Claude cannot invoke those itself.

## Steps

1. Read cheap context only: the user's prompt, the project's `CLAUDE.md`/`README.md` (first ~40 lines), and the top-level files (`package.json`, `pyproject.toml`, `Package.swift`, `app.json`, folder names).
2. Match against the catalog below.
3. Reply with one short block: `Context: <what you detected>. Suggested: <skills>.` Mark manual-only ones with the exact command to type. Then continue with the task.
4. Suggest once per session. If you already suggested, or nothing fits, say nothing.

## Catalog

| Context | Auto-selected by Claude | Manual-only (suggest the command) |
|---|---|---|
| Any coding task (write, fix, refactor) | karpathy-guidelines | `/ponytail` (minimal solution); `/ponytail-review` for diffs, `/ponytail-audit` for a whole repo |
| Web UI, components, motion | emil-design-eng, animate, apple-design, find-animation-opportunities, improve-animations, animation-vocabulary | `/prototype` (compare UI variants), `/review-animations`, `/pick-ui-library` |
| React Native / Expo | animate-expo | `/pick-ui-library` |
| Toasts / Sonner | ask-sonner | |
| Swift / iOS | write-swift | |
| Documents, posters, themed artifacts | canvas-design, theme-factory, brand-guidelines, artifacts-builder | |
| Marketing, copy, SEO, ads, sales, pricing | the matching marketingskills (copywriting, seo-audit, cro, ads, cold-email, pricing, ...); start with product-marketing in a new project | |

## Project-scoped install (only when the user asks)

Global installs stay global. If a project clearly needs only a subset, offer a project-level install (no `-g`), for example:

`npx skills@latest add Loek2505/claude-skills -y --skill animate --skill apple-design`

Never run it without the user's yes.
