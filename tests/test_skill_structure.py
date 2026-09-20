from pathlib import Path
import re
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SKILL.read_text(encoding="utf-8")
        parts = cls.text.split("---", 2)
        if len(parts) != 3:
            raise AssertionError("SKILL.md must contain YAML frontmatter")
        cls.frontmatter = yaml.safe_load(parts[1])

    def test_required_metadata(self):
        self.assertEqual(self.frontmatter["name"], "saas-commercialization")
        description = self.frontmatter["description"]
        self.assertIsInstance(description, str)
        self.assertGreater(len(description), 40)
        self.assertLessEqual(len(description), 1024)

    def test_name_uses_agent_skills_format(self):
        self.assertRegex(
            self.frontmatter["name"],
            r"^[a-z0-9]+(?:-[a-z0-9]+)*$",
        )

    def test_entrypoint_is_focused(self):
        self.assertLessEqual(len(self.text.splitlines()), 500)

    def test_references_exist(self):
        references = re.findall(r"\]\((references/[^)]+)\)", self.text)
        self.assertGreater(len(references), 0)
        missing = [path for path in references if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_no_scaffold_placeholders(self):
        files = [SKILL, *sorted((ROOT / "references").glob("*.md"))]
        unfinished = []
        for path in files:
            content = path.read_text(encoding="utf-8")
            if "[TODO" in content or "PLACEHOLDER" in content:
                unfinished.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(unfinished, [])

    def test_openai_interface_metadata(self):
        metadata = yaml.safe_load(
            (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        )
        interface = metadata["interface"]
        self.assertTrue(interface["display_name"])
        self.assertTrue(interface["short_description"])
        self.assertIn("$saas-commercialization", interface["default_prompt"])


if __name__ == "__main__":
    unittest.main()
