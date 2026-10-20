# claude-skills

Persoonlijke verzameling Claude Code skills, zodat ze met één commando op elk device beschikbaar zijn.

## Installeren (op elk nieuw device)

```bash
npx skills@latest add Loek2505/claude-skills -g -y --all
```

Ponytail-skills staan op handmatig (`disable-model-invocation: true`): aanroepen met `/ponytail` enz. De `skill-router` suggereert wanneer dat handig is.

## Bijwerken

```bash
npx skills@latest update -g
```

## Inhoud

- **Emil Kowalski** (animate, animate-expo, animation-vocabulary, apple-design, ask-sonner, emil-design-eng, find-animation-opportunities, improve-animations, pick-ui-library, prototype, review-animations, write-swift) — bron: [emilkowalski/skills](https://github.com/emilkowalski/skills), MIT-licentie in `licenses/`
- **ComposioHQ document/artifact-tools** (artifacts-builder, brand-guidelines, canvas-design, theme-factory) — bron: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- **Corey Haines marketingskills** (50 skills: copywriting, seo-audit, cro, pricing, cold-email, ads, enz.) — bron: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), MIT-licentie in `licenses/`
- **Ponytail** (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review — minimalistisch coderen/over-engineering reviewen) — bron: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), MIT-licentie in `licenses/`
- **skill-router** (eigen) — adviseert per project/prompt welke skills passen en welke handmatige skills (ponytail*, prototype, pick-ui-library, review-animations) je moet aanzetten
- **Andrej Karpathy** (karpathy-guidelines) — bron: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

## Overzicht (75 skills)

| Groep | Aantal | Start |
|---|---|---|
| Marketing (Corey Haines) | 50 | Automatisch |
| Design en animatie (Emil Kowalski) | 12 | Automatisch, behalve `prototype`, `pick-ui-library` en `review-animations` (handmatig) |
| Documenten en artifacts (ComposioHQ) | 4 | Automatisch |
| Ponytail | 6 | Handmatig |
| Karpathy-richtlijnen | 1 | Automatisch |
| skill-router (eigen) | 1 | Automatisch |

Laatste controle en verbetervoorstellen: zie [`AUDIT.md`](AUDIT.md).

## Niet in dit repo

- **Composio `connect-apps` MCP-server** — bevat een persoonlijke API-key en moet per device apart worden opgezet met `claude mcp add`.
- **ECC (Affaan)** — is een aparte Claude Code plugin-marketplace, geen skill. Op elk device:
  ```bash
  claude plugin marketplace add affaan-m/ECC
  claude plugin install ecc@ecc
  ```
