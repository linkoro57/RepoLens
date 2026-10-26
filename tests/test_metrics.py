import tempfile
import unittest
from pathlib import Path
from repolens.core.metrics import count_lines, format_size

class MetricsTests(unittest.TestCase):
    def test_counts_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "file.py"
            path.write_text("one\ntwo\n", encoding="utf-8")
            self.assertEqual(count_lines(path, path.stat().st_size), 2)

    def test_formats_size(self):
        self.assertEqual(format_size(1024), "1.0 KB")
