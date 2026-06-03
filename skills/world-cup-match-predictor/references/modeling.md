# Modeling Reference

Use this reference when a user asks for the technical basis of a World Cup forecast or when you need to build the probability estimate.

## Research Lineage

Rahul Savani's public research context is method inspiration, not content filler. Relevant ideas include algorithmic game theory, automated trading, agent-based modeling, reinforcement learning, sports betting markets, market microstructure, and risk-aware evaluation.

Useful public sources:

- [University of Liverpool research profile](https://www.liverpool.ac.uk/people/rahul-savani/research)
- [Rahul Savani publications](https://cgi.csc.liv.ac.uk/~rahul/publications.html)
- [Market Making via Reinforcement Learning](https://arxiv.org/abs/1804.04216)
- [Robust Market Making via Adversarial Reinforcement Learning](https://arxiv.org/abs/2003.01820)

Map the research into the predictor this way:

- Odds are market prices, not betting instructions.
- Market prices imply probabilities, but need no-vig normalization.
- Forecasts should manage uncertainty like inventory risk: publish a full distribution, not only a winner.
- Robustness matters: robustness means not letting one source, one price, or one rumor dominate.
- Evaluation matters: use proper scoring rules rather than win-rate storytelling.

## Decimal Odds To No-Vig Probability

For 1X2 decimal odds:

```text
raw implied probability = 1 / decimal odds
overround = sum(raw implied probabilities)
no-vig probability = raw probability / overround
```

Use `scripts/normalize_odds.py` for deterministic conversion:

```bash
python3 scripts/normalize_odds.py 1.80 3.60 4.80
```

Do not copy sportsbook percentages directly into the final forecast. State source, retrieval time, and whether the probability is raw or no-vig.

## Explainable Ensemble

Use a conservative ensemble:

| Component | Purpose | Typical treatment |
| --- | --- | --- |
| Team strength prior | Baseline quality | Elo, FIFA ranking, power rating |
| Football goal model | Match mechanics | Poisson or xG-informed goal distribution |
| Market prior | Aggregated public/private information | no-vig 1X2 probability |
| Context adjustments | Match-specific shifts | injuries, suspensions, rest, venue, weather |
| Calibration | Avoid false precision | round public output; reduce confidence on missing data |

If inputs are thin, lean more on market and strength priors but lower confidence.

## Poisson Sketch

If expected goals are available:

1. Estimate `lambda_a` and `lambda_b`.
2. Calculate scoreline probabilities for 0-0 through a practical cap such as 6-6.
3. Sum scorelines where A goals > B goals for team A win.
4. Sum equal scorelines for draw.
5. Sum B goals > A goals for team B win.

Use this as a football structure model, not as a replacement for market signals.

## Robustness And Sensitivity

Run sensitivity checks when a major player, goalkeeper, or tactical setup is uncertain:

| Scenario | Expected effect |
| --- | --- |
| Core attacker out | Reduce that team's win probability and expected goals |
| First-choice goalkeeper out | Increase opponent scoring probability |
| Heavy rotation | Lower confidence; widen draw probability |
| Sharp market move | Explain possible information flow before adjusting |

## Evaluation

Use proper scoring rules and calibration checks:

- Brier score: lower is better for probability accuracy.
- Log loss: penalizes overconfident wrong forecasts.
- Calibration curve: events forecast at 60% should happen about 60% of the time.
- Closing-line comparison: compare model probabilities with late market probabilities.

Avoid judging by single-match correctness. A good probability forecast can be wrong in one match and still be well-calibrated.
