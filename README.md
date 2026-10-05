# claude-skills

Persoonlijke verzameling Claude Code skills, zodat ze met één commando op elk device beschikbaar zijn.

## Installeren (op elk nieuw device)

```bash
npx skills@latest add loekwesterhof/claude-skills -g -y --all
```

## Bijwerken

```bash
npx skills@latest update -g
```

## Inhoud

- **Emil Kowalski** (animate, animate-expo, animation-vocabulary, apple-design, ask-sonner, emil-design-eng, find-animation-opportunities, improve-animations, pick-ui-library, prototype, review-animations, write-swift) — bron: [emilkowalski/skills](https://github.com/emilkowalski/skills)
- **ComposioHQ document/artifact-tools** (artifacts-builder, brand-guidelines, canvas-design, theme-factory) — bron: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- **Corey Haines marketingskills** (50 skills: copywriting, seo-audit, cro, pricing, cold-email, ads, enz.) — bron: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), MIT-licentie in `licenses/`
- **Ponytail** (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review — minimalistisch coderen/over-engineering reviewen) — bron: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), MIT-licentie in `licenses/`
- **Andrej Karpathy** (karpathy-guidelines) — bron: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

## Niet in dit repo

- **Composio `connect-apps` MCP-server** — bevat een persoonlijke API-key en moet per device apart worden opgezet met `claude mcp add`.
- **ECC (Affaan)** — is een aparte Claude Code plugin-marketplace, geen skill. Op elk device:
  ```bash
  claude plugin marketplace add affaan-m/ECC
  claude plugin install ecc@ecc
  ```
