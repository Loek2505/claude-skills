# claude-skills

Persoonlijke verzameling Claude Code skills, zodat ze met één commando op elk device beschikbaar zijn.

## Installeren (op elk nieuw device)

```bash
npx skills@latest add Loek2505/claude-skills -g -y --all
```

Een deel van de skills staat op handmatig (`disable-model-invocation: true`): Ponytail, een paar design-skills en de app/SaaS-skills. Claude kiest die niet zelf, en hun beschrijving kost dus geen tokens per prompt. Aanroepen met `/naam`, bijvoorbeeld `/ponytail` of `/aso`. De `skill-router` suggereert wanneer dat handig is.

## Bijwerken

```bash
npx skills@latest update -g
```

## Bijwerken vanuit de bronnen

`npx skills update` haalt de skills uit déze repo, niet uit de bronnen. Bij een update vanuit een bron (laatst: 20 okt 2026) moeten deze eigen aanpassingen terug:

- `disable-model-invocation: true` op alle ponytail-skills en de app/SaaS-skills uit het overzicht hieronder
- de beschrijving van `emil-design-eng` (met "Use when …")

## Inhoud

- **Emil Kowalski** (animate, animate-expo, animation-performance, animation-vocabulary, apple-design, ask-sonner, break-ui, emil-design-eng, find-animation-opportunities, improve-animations, mobile-native, pick-ui-library, prototype, review-animations, write-swift) — bron: [emilkowalski/skills](https://github.com/emilkowalski/skills), MIT-licentie in `licenses/`
- **ComposioHQ document/artifact-tools** (artifacts-builder, brand-guidelines, canvas-design, theme-factory) — bron: [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- **Corey Haines marketingskills** (52 skills: copywriting, seo-audit, cro, pricing, cold-email, ads, link-building, enz.) — bron: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), MIT-licentie in `licenses/`
- **Ponytail** (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review — minimalistisch coderen/over-engineering reviewen) — bron: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), MIT-licentie in `licenses/`
- **skill-router** (eigen) — adviseert per project/prompt welke skills passen en welke handmatige skills je moet aanzetten
- **Andrej Karpathy** (karpathy-guidelines) — bron: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

## Overzicht (79 skills)

| Groep | Aantal | Start |
|---|---|---|
| Marketing (Corey Haines) | 52 | Automatisch, behalve 13 app/SaaS-skills (handmatig): `aso`, `signup`, `onboarding`, `paywalls`, `popups`, `churn-prevention`, `referrals`, `launch`, `free-tools`, `programmatic-seo`, `directory-submissions`, `influencer-marketing`, `sms` |
| Design en animatie (Emil Kowalski) | 15 | Automatisch, behalve `prototype`, `pick-ui-library`, `review-animations`, `write-swift` en `animate-expo` (handmatig) |
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
