# Audit claude-skills (oktober 2026)

Gecontroleerd: 75 skills op frontmatter, naam versus mapnaam, beschrijvingen, verwijzingen naar bestanden, `evals.json`, overlap, licenties en privégegevens.

Wat mechanisch te repareren was, is gerepareerd (zie [Uitgevoerd](#uitgevoerd)). Al het andere hieronder zijn **voorstellen**. Er is niets verwijderd of samengevoegd.

## Uitgevoerd

| Commit | Wat |
|---|---|
| README-installatiecommando | Wees naar `loekwesterhof/claude-skills`, een repo die niet bestaat. Nu `Loek2505/claude-skills`, gelijk aan `skill-router`. |
| Licentie Emil Kowalski | `emilkowalski/skills` is MIT, maar de licentietekst ontbrak. Toegevoegd als `licenses/emilkowalski-LICENSE`; de README verwijst ernaar. |
| `emil-design-eng` | De beschrijving zei niet wanneer de skill moet starten. Er staat nu een "Use when …"-zin in, zodat Claude hem zelf kan kiezen. |

## Privacy en veiligheid (repo is openbaar)

- Geen API-keys, tokens, wachtwoorden of privésleutels gevonden.
- Geen gegevens over Loek, SW Vastgoedverbetering, Saxion of corporaties in de skills.
- De enige e-mailadressen in bestanden zijn die van font-ontwerpers in de OFL-licenties van `canvas-design`. Die horen daar.
- **Let op:** de commits staan op naam van `loek.westerhof@gmail.com`, en dat adres is zichtbaar voor iedereen die de geschiedenis bekijkt. Wil je dat niet, zet dan in GitHub *Settings → Emails* "Keep my email addresses private" aan en gebruik voortaan het `@users.noreply.github.com`-adres.

## Licenties

| Bron | Licentie | Status |
|---|---|---|
| emilkowalski/skills | MIT | Nu toegevoegd |
| coreyhaines31/marketingskills | MIT | Aanwezig |
| DietrichGebert/ponytail | MIT | Aanwezig |
| ComposioHQ (artifacts-builder, brand-guidelines, canvas-design, theme-factory) | Apache 2.0 | `LICENSE.txt` per skill aanwezig |
| multica-ai/andrej-karpathy-skills | MIT (volgens hun README) | **Voorstel:** de bronrepo heeft geen apart licentiebestand. `license: MIT` in de frontmatter is voldoende, maar een verwijzing in de README maakt het compleet. |

## Voorstellen

### 1. `brand-guidelines` — besloten: laten staan
Niet elk project hoeft in de stijl van SW. De skill blijft zoals hij is.

### 2. Dubbel geïnstalleerde skills — besloten: opruimen zonder functionaliteit te verliezen
**Emil Kowalski-skills (12 stuks).** Deze staan zowel in deze repo als in het claude.ai-account (als plugin). Vergelijking per bestand: de accountversies zijn **ouder en korter**. Voorbeelden: `apple-design` 154 vs 282 regels, `write-swift` 238 vs 388. Bij `animate`, `animate-expo`, `ask-sonner`, `improve-animations`, `prototype` en `review-animations` ontbreken in het account de hulpbestanden (`RECIPES.md`, `API.md`, `AUDIT.md`, `PLAN-TEMPLATE.md`, `PICKER.md`, `STANDARDS.md`).
- **Actie:** de repo blijft de bron. Vervang in claude.ai de oude versies door die uit deze repo. Haal er niets uit de repo weg, want dan gaat juist de complete versie verloren.

**Plugins (`searchfit-seo`, `marketing`, `sales`).** Deze overlappen met marketingskills uit de repo, maar elk heeft functies die de ander mist:
- `searchfit-seo` heeft `broken-links`, `keyword-clustering` en `content-translation`; de repo niet.
- `sales` en `marketing` werken met gekoppelde tools (CRM, mail, agenda); de repo-skills niet.
- De repo-skills zijn inhoudelijk uitgebreider (playbooks, `references/`).
- **Actie:** niets verwijderen. Dat zou functionaliteit kosten.

### 3. Overlap binnen de repo (prioriteit: laag)
Deze paren zijn bewust gescheiden en verwijzen al naar elkaar. Samenvoegen is **niet** nodig, maar weet dat ze tegelijk kunnen starten:
- `competitor-profiling` (onderzoek) ↔ `competitors` (vergelijkingspagina's)
- `ads` (campagnes) ↔ `ad-creative` (teksten en beelden)
- `copywriting` (nieuw) ↔ `copy-editing` (bestaand)
- `cro` ↔ `signup`, `popups`, `paywalls`, `onboarding`
- `analytics` (tracking) ↔ `attribution` (interpretatie)
- `emails` ↔ `cold-email` ↔ `sms`
- `emil-design-eng` ↔ `animate` ↔ `apple-design` ↔ `review-animations` ↔ `improve-animations`

### 4. Lengte van skills (prioriteit: laag)
De richtlijn is maximaal ~500 regels per `SKILL.md`; langere stukken horen in `references/`.
- `emil-design-eng`: 674 regels
- `ads`: 507 regels

Voorstel: bij `emil-design-eng` de lange voorbeeldsecties naar een `references/`-bestand verplaatsen. Pas dit liever upstream aan, anders gaat het verloren bij een update van de bron.

### 5. `review-animations`-beschrijving (prioriteit: laag)
Kort en zonder "Use when". De skill staat op handmatig (`/review-animations`), dus het werkt; alleen `skill-router` leunt op de beschrijving. Niet aangepast omdat het geen probleem geeft.

### 6. Skills voor apps en SaaS — besloten: laten staan
Kunnen later nog van pas komen. Wie per project minder ruis wil, kan de project-install uit `skill-router` gebruiken.

<details><summary>Oorspronkelijke analyse</summary>

Veel marketingskills zijn gericht op SaaS en consumentenapps (`aso`, `paywalls`, `popups`, `signup`, `churn-prevention`, `sms`, `directory-submissions`, `influencer-marketing`). Voor B2B-werk richting woningcorporaties zijn vooral `cold-email`, `prospecting`, `customer-research`, `events`, `product-marketing`, `marketing-psychology` en `sales-enablement` nuttig. De rest uitzetten scheelt ruis bij het kiezen van skills. Dat kan per project met de project-install uit `skill-router`, zonder iets uit de repo te halen.

</details>

## Gecontroleerd zonder bevindingen
- Alle 75 mappen hebben een `SKILL.md` met geldige frontmatter, en `name` is gelijk aan de mapnaam.
- Alle 50 `evals/evals.json` zijn geldige JSON.
- Verwijzingen naar `references/`-bestanden van andere skills (zoals `ads/references/conversion-tracking.md`) bestaan allemaal.
- Links als `/features/analytics` en `[Terms](link)` zijn voorbeeldtekst, geen kapotte links.
- De telling in de README (50 marketingskills) klopt.
