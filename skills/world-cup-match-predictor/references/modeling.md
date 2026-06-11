# Modeling Reference

Use this reference when a user asks for the technical basis of a World Cup forecast or when you need to build the probability estimate.

## Research Lineage

Present the model as an integration of field-level research, not as the work of any single person. The public skill should internalize several mature research traditions, organized below by theme. Every source uses a durable publisher DOI or stable repository link so the lineage stays valid over time.

### Football score modeling

- [Modelling association football scores, Maher, 1982 — Statistica Neerlandica](https://doi.org/10.1111/j.1467-9574.1982.tb00782.x)
- [Modelling association football scores and inefficiencies in the football betting market, Dixon & Coles, 1997 — JRSS Series C](https://doi.org/10.1111/1467-9876.00065)
- [A dynamic bivariate Poisson model for forecasting EPL match results, Koopman & Lit, 2015 — JRSS Series A](https://doi.org/10.1111/rssa.12042)

### Odds as market-implied probabilities

- [Prices of state contingent claims with insider traders, and the favourite-longshot bias, Shin, 1992 — The Economic Journal](https://doi.org/10.2307/2234526)
- [On determining probability forecasts from betting odds, Štrumbelj, 2014 — International Journal of Forecasting](https://doi.org/10.1016/j.ijforecast.2014.01.006)

### Fixed-odds market efficiency and rating-based forecasting

- [Modelling football match results and the efficiency of fixed-odds betting, Goddard, 2005 — stable mirror](https://www.stat.berkeley.edu/users/aldous/157/Papers/goddard.pdf)
- [Using ELO ratings for match result prediction in association football, Hvattum & Arntzen, 2010 — International Journal of Forecasting](https://doi.org/10.1016/j.ijforecast.2009.10.002)

### Market microstructure and inventory-risk intuition

- [High-frequency trading in a limit order book, Avellaneda-Stoikov, 2008 — Quantitative Finance](https://doi.org/10.1080/14697680701381228)

### Proper scoring rules, calibration, and evaluation

- [Strictly proper scoring rules, prediction, and estimation, Gneiting & Raftery, 2007 — JASA](https://doi.org/10.1198/016214506000001437)
- [Evaluating probabilistic forecasts of football matches, Wheatcroft, 2019 — arXiv](https://arxiv.org/abs/1908.08980)

These traditions map onto the components below: score models supply match mechanics, odds-to-probability methods (no-vig and Shin) turn prices into priors, rating and efficiency work calibrates the strength prior, microstructure supplies the inventory-risk stance on uncertainty, and scoring rules govern evaluation.

Map the research into the predictor this way:

- Odds are market prices, not betting instructions.
- Market prices imply probabilities, but need no-vig normalization.
- Football score models provide structure for low-scoring outcomes and draw probability.
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

## Poisson And Dixon-Coles Sketch

If expected goals are available:

1. Estimate `lambda_a` and `lambda_b`.
2. Calculate scoreline probabilities for 0-0 through a practical cap such as 6-6.
3. Sum scorelines where A goals > B goals for team A win.
4. Sum equal scorelines for draw.
5. Sum B goals > A goals for team B win.
6. Apply a Dixon-Coles style low-score adjustment only when the data and implementation justify it.

Use this as a football structure model, not as a replacement for market signals.

## Market Microstructure And Inventory-Risk Intuition

The skill does not run a trading system. It borrows a conservative idea from market microstructure: a good market-facing model manages exposure to uncertainty.

Translate that into forecasting behavior:

- publish the whole 1X2 distribution,
- avoid one-outcome certainty,
- mark fragile information as uncertainty,
- show market vs model differences,
- lower confidence when sources are stale, conflicted, or thin.

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
