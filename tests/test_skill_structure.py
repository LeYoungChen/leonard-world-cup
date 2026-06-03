import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "world-cup-match-predictor"


class SkillStructureTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "SKILL.md",
            "agents/openai.yaml",
            "references/modeling.md",
            "references/public-positioning.md",
            "references/output-formats.md",
            "scripts/normalize_odds.py",
        ]

        missing = [path for path in required if not (SKILL_DIR / path).is_file()]

        self.assertEqual(missing, [])

    def test_skill_frontmatter_and_triggers_are_portable(self):
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("name: world-cup-match-predictor", text)
        self.assertIn("description:", text)
        self.assertIn("World Cup", text)
        self.assertIn("cross-agent", text)
        self.assertIn("clickable", text)
        self.assertIn("Do not provide stake sizing", text)

    def test_references_cover_modeling_positioning_and_outputs(self):
        modeling = (SKILL_DIR / "references" / "modeling.md").read_text(encoding="utf-8")
        positioning = (SKILL_DIR / "references" / "public-positioning.md").read_text(encoding="utf-8")
        outputs = (SKILL_DIR / "references" / "output-formats.md").read_text(encoding="utf-8")

        for phrase in ["no-vig", "Brier score", "Rahul Savani", "robustness"]:
            self.assertIn(phrase, modeling)

        for phrase in ["not betting advice", "forbidden", "clickable source"]:
            self.assertIn(phrase, positioning)

        for phrase in ["Markdown table", "JSON", "Mermaid", "source table"]:
            self.assertIn(phrase, outputs)

    def test_openai_yaml_has_required_interface_fields(self):
        text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")

        self.assertIn('display_name: "World Cup Match Predictor"', text)
        self.assertIn('short_description:', text)
        self.assertIn('default_prompt:', text)
        self.assertIn("$world-cup-match-predictor", text)


if __name__ == "__main__":
    unittest.main()
