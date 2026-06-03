import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "world-cup-match-predictor" / "scripts" / "normalize_odds.py"


def load_module():
    spec = importlib.util.spec_from_file_location("normalize_odds", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NormalizeOddsTests(unittest.TestCase):
    def test_converts_decimal_odds_to_raw_implied_probabilities(self):
        module = load_module()

        raw = module.raw_implied_probabilities([2.0, 3.5, 4.0])

        self.assertAlmostEqual(raw["team_a_win"], 0.5)
        self.assertAlmostEqual(raw["draw"], 1 / 3.5)
        self.assertAlmostEqual(raw["team_b_win"], 0.25)

    def test_removes_overround_to_sum_to_one(self):
        module = load_module()

        raw = module.raw_implied_probabilities([1.8, 3.6, 4.8])
        no_vig = module.normalize_no_vig(raw)

        self.assertAlmostEqual(sum(no_vig.values()), 1.0)
        self.assertGreater(no_vig["team_a_win"], no_vig["draw"])
        self.assertGreater(no_vig["draw"], no_vig["team_b_win"])

    def test_rejects_invalid_decimal_odds(self):
        module = load_module()

        with self.assertRaisesRegex(ValueError, "greater than 1.0"):
            module.raw_implied_probabilities([1.0, 3.2, 5.0])

    def test_percentages_are_corrected_to_total_100(self):
        module = load_module()

        percentages = module.to_percentages(
            {"team_a_win": 1 / 3, "draw": 1 / 3, "team_b_win": 1 / 3},
            decimals=0,
        )

        self.assertEqual(sum(percentages.values()), 100)
        self.assertEqual(set(percentages), {"team_a_win", "draw", "team_b_win"})

    def test_cli_outputs_json_with_raw_and_no_vig_probabilities(self):
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "1.8", "3.6", "4.8"],
            check=True,
            text=True,
            capture_output=True,
        )

        payload = json.loads(completed.stdout)
        self.assertEqual(payload["input_decimal_odds"]["team_a_win"], 1.8)
        self.assertAlmostEqual(sum(payload["no_vig_probabilities"].values()), 1.0)
        self.assertEqual(sum(payload["no_vig_percentages"].values()), 100.0)


if __name__ == "__main__":
    unittest.main()
