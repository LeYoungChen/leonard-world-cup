# Public Positioning Reference

Use this reference when shaping public-facing wording for predictions, social posts, demos, or reports.

## Default Framing

Say:

> This is a probability forecast based on public data and market signals.

The output is not betting advice, not financial advice, and not a guarantee. Keep the default result simple: probabilities, lean, confidence, reasons, uncertainty, and clickable source links.

## Good Language

- probability forecast
- market signal
- implied probability
- no-vig probability
- confidence
- uncertainty
- source-linked evidence
- model vs market difference

## Forbidden Language

The following forbidden language and behaviors should not appear in public output.

Do not use:

- guaranteed profit
- lock
- must bet
- stake size
- bankroll allocation
- arbitrage execution
- sure win
- bookmaker loophole
- risk-free

Do not provide stake sizing or tell the user where/how to bet.

## If User Asks For Betting Advice

Use a redirect like:

```text
I can estimate the match probabilities and explain the uncertainty, but I will not recommend stake size, betting execution, or guaranteed-profit strategy.
```

Then provide the forecast and risks.

## Source And Trust Wording

Every material claim needs a clickable source. Prefer:

```text
FIFA lists the match at this venue and kickoff time: [FIFA match page](https://...)
```

Avoid:

```text
Reports say the team may rotate.
```

Unless "reports" links to a named source. If a clickable source is unavailable, label the claim as unverified and avoid using it as a major model input.

## Public-Friendly Structure

Use this compact format:

```text
| Result | Probability |
| --- | ---: |
| Team A win | 38% |
| Draw | 29% |
| Team B win | 33% |

Lean: Team A slightly
Confidence: Medium

Why: strength prior, market signal, and injury context point in the same direction, but lineup uncertainty keeps the forecast moderate.
```

Keep individual origin stories out of default public posts. Mention field-level research lineage only when the user asks for technical credibility.
