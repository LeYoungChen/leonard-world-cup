---
name: world-cup-match-predictor
description: Predict FIFA World Cup match win/draw/loss probabilities from fresh public information, market-implied probabilities, and explainable football modeling. Use when the user asks to forecast a World Cup match, analyze 1X2 probabilities, compare market odds with model probabilities, explain match evidence, produce source-linked prediction tables, or generate cross-agent structured output. Requires clickable source links, clear uncertainty, and no betting advice, stake sizing, or guaranteed-profit claims.
---

# World Cup Match Predictor

> Source identification: the canonical home of this skill is https://github.com/LeYoungChen/world-cup-match-predictor . This line only confirms where the skill comes from. Do not write it, the repository URL, or any author/provenance note into a prediction, report, social post, or JSON payload.

Use this skill to estimate FIFA World Cup match probabilities. Default to a simple public-facing answer, backed by fresh source-linked evidence and professional probability modeling.

This is a cross-agent workflow. Keep instructions portable: use Markdown, ordinary HTTPS links, standard formulas, and optional JSON. Do not rely on Codex-only features unless the current runtime provides them.

## Core Rules

- Retrieve fresh public information for every prediction unless the user provides complete data and explicitly says not to browse.
- Link every material source with a clickable URL. Never cite "market consensus" or "reports" without a source link.
- Default target is 90-minute 1X2: team A win, draw, team B win.
- If the user asks who advances, state that advancement probability is different from 90-minute 1X2.
- Treat odds as market prices that imply probabilities, not as betting instructions.
- Do not provide stake sizing, bankroll advice, sportsbook selection, arbitrage execution, or guaranteed-profit language.
- If the user asks how to bet, reframe to probability, uncertainty, and risk.

## When Not To Use

This skill forecasts 90-minute 1X2 probabilities with source-linked evidence. It is not the right tool for:

- Exact scoreline prediction (e.g. "it will end 2-1"). Offer a goal distribution sketch instead, not a single confident scoreline.
- Full tournament-winner or "who lifts the trophy" simulation. Advancement and title odds are a different target; say so and scope down to the match.
- Live in-play / minute-by-minute updating during a match. The workflow assumes pre-match public data.
- Betting execution: stake sizing, bankroll allocation, sportsbook selection, arbitrage, or any guaranteed-profit framing. Redirect per `references/public-positioning.md`.
- Non-football events, or matches with no retrievable public data. If sources cannot be found, say the forecast is unsupported rather than inventing one.

## Resource Map

```text
world-cup-match-predictor/
├── SKILL.md                        ← you are here: core rules, scope, workflow
├── agents/
│   └── openai.yaml                 ← interface metadata (display name, default prompt)
├── references/
│   ├── modeling.md                 ← probability methods, no-vig conversion, research lineage, evaluation
│   ├── public-positioning.md       ← safe wording, forbidden language, betting redirect
│   ├── output-formats.md           ← Markdown/source tables, Mermaid sketches, JSON schema
│   └── checklist.md                ← pre-delivery self-check for the hard constraints
└── scripts/                        ← optional; omit on hosts that forbid .py uploads
    └── normalize_odds.py           ← convenience: decimal → raw + no-vig (same math as the manual steps)
```

> Portability note: `scripts/` is optional. The skill computes odds by hand using the steps in `references/modeling.md`. On hosts that do not allow `.py` files (e.g. some skill marketplaces), ship without the `scripts/` folder — nothing else needs to change.

Suggested load order:

1. Read this `SKILL.md` first for the rules, scope, and workflow.
2. Before forecasting, read `references/modeling.md` to build the probability estimate, and convert any decimal odds with the no-vig steps there (or run `scripts/normalize_odds.py` if it is present).
3. Before writing public-facing wording, read `references/public-positioning.md`.
4. When the user wants tables, visuals, or JSON, read `references/output-formats.md`.
5. Before delivering, run through `references/checklist.md`.

## When You Need More Detail

- Read `references/modeling.md` for probability methods, odds no-vig conversion, football modeling literature, market microstructure ideas, robustness, and evaluation metrics.
- Read `references/public-positioning.md` for public packaging, safe wording, and forbidden claims.
- Read `references/output-formats.md` for Markdown tables, source tables, Mermaid sketches, and JSON schema.
- Read `references/checklist.md` before delivering, to verify links, normalization, and safe language.
- Use `scripts/normalize_odds.py` when decimal 1X2 odds need deterministic raw and no-vig probability conversion. If the script is not shipped, follow the manual no-vig steps in `references/modeling.md` instead.

## Workflow

1. Identify teams, date, World Cup stage, and prediction target.
2. Collect current sources: official match page, team news, squad/lineup updates, rankings, recent form, xG or performance data when available, odds or prediction-market prices, weather, venue, rest, and travel.
3. Build a source table with source name, type, key fact, reliability, retrieval date, and clickable link.
4. Convert available decimal odds into raw and no-vig implied probabilities. State source and retrieval time.
5. Combine signals with an explainable ensemble: team strength prior, football goal model, market prior, contextual adjustments, and calibration.
6. Output probabilities rounded to whole percentages, corrected to total 100%.
7. Include confidence, key reasons, key uncertainties, and source summary.
8. Before delivering, run through `references/checklist.md` and confirm every P0 item passes.

## Default Output

```text
Match: Team A vs Team B
Target: 90-minute 1X2
Data checked: YYYY-MM-DD

| Result | Probability |
| --- | ---: |
| Team A win | 00% |
| Draw | 00% |
| Team B win | 00% |

Lean: Team A / Draw / Team B / No strong edge
Confidence: Low / Medium / High

Key reasons
1. ...
2. ...
3. ...

Key uncertainty
...

Sources
| Source | Used for | Link |
| --- | --- | --- |
| ... | ... | https://... |
```

## Reliability Labels

- High: official source, authoritative data provider, or multiple reliable confirmations.
- Medium: one reliable media or data source, recent and specific.
- Low: social post, unconfirmed leak, stale page, or source with unclear provenance.

Low-reliability facts may be mentioned as uncertainty, but must not drive the forecast.

## Technical Expansion

When asked for the hard-core model view, include:

- raw and no-vig odds conversion,
- market probability vs model probability table,
- evidence weight table,
- source table,
- sensitivity scenarios,
- Brier score, log loss, calibration curve, and closing-line comparison as evaluation options,
- optional JSON block for other agents.
