# Pre-Delivery Checklist

Run through this before delivering any forecast. It turns the hard constraints in `SKILL.md` and `public-positioning.md` into a verifiable list. P0 items must all pass; a P0 failure means the output is not safe to ship.

## P0 · Must pass

- [ ] Every material claim has a clickable source link. No "market consensus", "reports say", or unlinked numbers driving the forecast.
- [ ] Probabilities are whole percentages and sum to exactly 100% (compute with the no-vig steps in `modeling.md`, or `scripts/normalize_odds.py` if shipped, to correct rounding drift).
- [ ] No forbidden language anywhere in the output: guaranteed profit, lock, must bet, stake size, bankroll allocation, arbitrage execution, sure win, bookmaker loophole, risk-free.
- [ ] No stake sizing, no sportsbook selection, no "how/where to bet". A betting-advice request is redirected to probability, uncertainty, and risk.
- [ ] Odds are presented as market-implied probabilities, not betting instructions. State source, retrieval time, and whether each probability is raw or no-vig.
- [ ] No provenance/source-identification line, repo URL, or research-lineage personal names appear in the delivered artifact.

## P1 · Quality

- [ ] Target is stated explicitly (default: 90-minute 1X2). If the user asked about advancement or the trophy, the answer notes that is a different target.
- [ ] Each source row carries a reliability label (High / Medium / Low) and a retrieval date.
- [ ] Low-reliability facts appear only as uncertainty, never as a primary model input.
- [ ] Confidence level is present and consistent with how thin/conflicted the sources are.
- [ ] Key reasons and key uncertainty are both included.
- [ ] Information is fresh: sources were retrieved for this match, not reused from a stale page.

## P2 · Polish

- [ ] When market vs model is shown, the difference column is in percentage points and the direction is explained.
- [ ] Mermaid is used only where the destination renders it; otherwise fall back to Markdown tables.
- [ ] Optional JSON block (if produced) validates against the schema in `output-formats.md` and its probabilities also sum to 1.0.
- [ ] Report-ready order is followed: short forecast → probability table → reasons → uncertainty → market vs model → source table → technical appendix if requested.
