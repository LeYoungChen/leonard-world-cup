# World Cup Match Predictor

A portable skill/workflow for estimating FIFA World Cup 90-minute win/draw/loss probabilities from fresh public information, market-implied probabilities, and explainable football modeling.

## What It Does

- Retrieves current public information for each match.
- Requires clickable source links for material claims.
- Converts 1X2 decimal odds into raw and no-vig implied probabilities.
- Produces a simple public-facing forecast with probability table, confidence, reasons, uncertainty, and sources.
- Supports technical expansion with market vs model comparison, evidence tables, sensitivity analysis, and JSON output.
- Avoids betting advice, stake sizing, sportsbook selection, and guaranteed-profit language.

## Skill Location

The portable skill lives at:

```text
skills/world-cup-match-predictor/
```

It can be used by Codex as a skill, or by other agents as a readable workflow:

- `SKILL.md` contains the core instructions.
- `references/modeling.md` explains the probability and market-signal logic.
- `references/public-positioning.md` defines public language and safety boundaries.
- `references/output-formats.md` defines tables, visual explanations, and JSON schema.
- `references/checklist.md` is the pre-delivery self-check for the hard constraints.
- `scripts/normalize_odds.py` provides deterministic odds conversion.

## Example

```text
Use $world-cup-match-predictor to estimate Argentina vs France 90-minute win/draw/loss probabilities with clickable sources.
```

Expected output shape:

```markdown
| Result | Probability |
| --- | ---: |
| Argentina win | 38% |
| Draw | 29% |
| France win | 33% |
```

The full answer should also include a lean, confidence level, key reasons, key uncertainties, and source table with clickable links.

## Odds Helper

```bash
python3 skills/world-cup-match-predictor/scripts/normalize_odds.py 1.80 3.60 4.80
```

The helper emits JSON with:

- input decimal odds,
- raw implied probabilities,
- overround,
- no-vig probabilities,
- rounded percentages corrected to total 100.

## Safety Boundary

This workflow is for probability forecasting and evidence explanation. It is not betting advice, financial advice, stake sizing, or an automated wagering system.

## Tests

```bash
python3 -m unittest discover -s tests -v
python3 /Users/chen/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/world-cup-match-predictor
```
