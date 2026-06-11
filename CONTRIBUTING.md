# Contributing

Thanks for helping improve `leonard-world-cup`.

This project is a portable Skill for AI agents that estimate FIFA World Cup 90-minute win/draw/loss probabilities from fresh public information, market-implied probabilities, and explainable football modeling. The most useful contributions are specific, reproducible, and tied to real forecast output.

## Before Opening an Issue

Please check whether the problem belongs to one of these buckets:

- Source discipline: a material claim is made without a clickable source link.
- Probability correctness: probabilities do not sum to 100%, or no-vig conversion looks wrong.
- Safety boundary: the output drifts into stake sizing, sportsbook selection, or guaranteed-profit language.
- Portability: the workflow relies on a runtime feature that is not available cross-agent.
- Documentation: rules, scope, modeling logic, output formats, or examples are unclear.

Concrete examples are much more useful than descriptions alone. If possible, include:

- The prompt or match you asked about.
- The full generated forecast (probability table, reasons, uncertainty, sources).
- The odds you fed in, if `normalize_odds.py` is involved.
- Which agent / runtime you used.

## Pull Request Guidelines

Keep PRs focused. A small fix with a reproducible example is easier to review than a large rewrite.

For changes to the skill's rules or scope:

- Do not weaken the safety boundary (no betting advice, stake sizing, or guaranteed-profit framing).
- Keep every material claim tied to a clickable source.
- Keep instructions portable across agents; do not add runtime-only dependencies without a fallback.

For changes to modeling or output:

- Run the test suite and the odds helper.
- Walk the `references/checklist.md` P0 items.

```bash
python3 -m unittest discover -s tests -v
python3 skills/leonard-world-cup/scripts/normalize_odds.py 1.80 3.60 4.80
```

## Good PRs Usually Include

- A short summary of the problem.
- The exact files changed.
- A before / after forecast example when behavior changes.
- Test or checklist notes.

## Style Notes

This Skill is opinionated by design. It prefers an explainable, source-linked forecast over a confident single answer, and it refuses betting advice on purpose. When in doubt, preserve the safety boundary and improve the evidence and explanation around it.
