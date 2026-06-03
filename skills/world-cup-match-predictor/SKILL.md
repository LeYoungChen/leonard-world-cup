---
name: world-cup-match-predictor
description: Predict FIFA World Cup match win/draw/loss probabilities from fresh public information, market-implied probabilities, and explainable football modeling. Use when the user asks to forecast a World Cup match, analyze 1X2 probabilities, compare market odds with model probabilities, explain match evidence, produce source-linked prediction tables, or generate cross-agent structured output. Requires clickable source links, clear uncertainty, and no betting advice, stake sizing, or guaranteed-profit claims.
---

# World Cup Match Predictor

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

## When You Need More Detail

- Read `references/modeling.md` for probability methods, odds no-vig conversion, Rahul Savani research lineage, robustness, and evaluation metrics.
- Read `references/public-positioning.md` for public packaging, safe wording, and forbidden claims.
- Read `references/output-formats.md` for Markdown tables, source tables, Mermaid sketches, and JSON schema.
- Use `scripts/normalize_odds.py` when decimal 1X2 odds need deterministic raw and no-vig probability conversion.

## Workflow

1. Identify teams, date, World Cup stage, and prediction target.
2. Collect current sources: official match page, team news, squad/lineup updates, rankings, recent form, xG or performance data when available, odds or prediction-market prices, weather, venue, rest, and travel.
3. Build a source table with source name, type, key fact, reliability, retrieval date, and clickable link.
4. Convert available decimal odds into raw and no-vig implied probabilities. State source and retrieval time.
5. Combine signals with an explainable ensemble: team strength prior, football goal model, market prior, contextual adjustments, and calibration.
6. Output probabilities rounded to whole percentages, corrected to total 100%.
7. Include confidence, key reasons, key uncertainties, and source summary.

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
