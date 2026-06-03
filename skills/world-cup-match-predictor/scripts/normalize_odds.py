#!/usr/bin/env python3
"""Convert 1X2 decimal odds into raw and no-vig implied probabilities."""

import argparse
import json
from typing import Dict, Iterable, List


OUTCOMES = ("team_a_win", "draw", "team_b_win")


def _validate_odds(odds: Iterable[float]) -> List[float]:
    values = [float(value) for value in odds]
    if len(values) != 3:
        raise ValueError("exactly three decimal odds are required")
    for value in values:
        if value <= 1.0:
            raise ValueError("decimal odds must be greater than 1.0")
    return values


def raw_implied_probabilities(odds: Iterable[float]) -> Dict[str, float]:
    """Return unnormalized implied probabilities for team A, draw, team B."""
    values = _validate_odds(odds)
    return {outcome: 1.0 / value for outcome, value in zip(OUTCOMES, values)}


def normalize_no_vig(raw: Dict[str, float]) -> Dict[str, float]:
    """Remove bookmaker overround by normalizing probabilities to sum to one."""
    missing = [outcome for outcome in OUTCOMES if outcome not in raw]
    if missing:
        raise ValueError(f"missing probabilities for: {', '.join(missing)}")

    total = sum(raw[outcome] for outcome in OUTCOMES)
    if total <= 0:
        raise ValueError("probabilities must sum to a positive number")
    return {outcome: raw[outcome] / total for outcome in OUTCOMES}


def to_percentages(probabilities: Dict[str, float], decimals: int = 1) -> Dict[str, float]:
    """Convert probabilities to percentages and correct rounding drift to 100."""
    if decimals < 0:
        raise ValueError("decimals must be non-negative")

    scale = 10**decimals
    percentages = {
        outcome: round(probabilities[outcome] * 100, decimals)
        for outcome in OUTCOMES
    }
    target = 100 * scale
    current = int(round(sum(value * scale for value in percentages.values())))
    drift_units = target - current

    if drift_units:
        largest = max(OUTCOMES, key=lambda outcome: probabilities[outcome])
        percentages[largest] = round(
            percentages[largest] + drift_units / scale,
            decimals,
        )

    if decimals == 0:
        return {outcome: int(percentages[outcome]) for outcome in OUTCOMES}
    return percentages


def build_payload(odds: Iterable[float], decimals: int = 1) -> Dict[str, object]:
    values = _validate_odds(odds)
    raw = raw_implied_probabilities(values)
    no_vig = normalize_no_vig(raw)
    return {
        "input_decimal_odds": {
            outcome: value for outcome, value in zip(OUTCOMES, values)
        },
        "raw_implied_probabilities": raw,
        "raw_implied_percentages": to_percentages(raw, decimals),
        "overround": sum(raw.values()),
        "no_vig_probabilities": no_vig,
        "no_vig_percentages": to_percentages(no_vig, decimals),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert 1X2 decimal odds into raw and no-vig probabilities."
    )
    parser.add_argument("team_a_win", type=float, help="Decimal odds for team A win")
    parser.add_argument("draw", type=float, help="Decimal odds for draw")
    parser.add_argument("team_b_win", type=float, help="Decimal odds for team B win")
    parser.add_argument(
        "--decimals",
        type=int,
        default=1,
        help="Decimal places for percentage output",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = build_payload(
        [args.team_a_win, args.draw, args.team_b_win],
        decimals=args.decimals,
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
