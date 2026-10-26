import unittest
from pathlib import Path
from repolens.core.languages import detect_language

class LanguageTests(unittest.TestCase):
    def test_detects_language_case_insensitively(self):
        self.assertEqual(detect_language(Path("main.PY")), "Python")

    def test_unknown_extension_returns_none(self):
        self.assertIsNone(detect_language(Path("file.unknown")))
