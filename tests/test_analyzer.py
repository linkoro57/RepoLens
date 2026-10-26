import tempfile
import unittest
from pathlib import Path
from repolens import RepositoryAnalyzer

class AnalyzerTests(unittest.TestCase):
    def test_analyzes_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Test", encoding="utf-8")
            (root / "LICENSE").write_text("Test", encoding="utf-8")
            (root / ".gitignore").write_text("__pycache__/", encoding="utf-8")
            (root / "main.py").write_text("message = 'hello'\nprint(message)\n", encoding="utf-8")
            report = RepositoryAnalyzer().analyze(root)
            self.assertEqual(report.main_language, "Python")
            self.assertEqual(len(report.files), 3)
            self.assertEqual(report.score, 100)

    def test_reports_missing_project_files(self):
        with tempfile.TemporaryDirectory() as directory:
            report = RepositoryAnalyzer().analyze(Path(directory))
            self.assertEqual({issue.code for issue in report.issues}, {"missing-readme", "missing-license", "missing-gitignore"})
            self.assertEqual(report.score, 74)
