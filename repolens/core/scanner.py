from pathlib import Path
from repolens.config import AnalyzerConfig
from repolens.core.languages import detect_language
from repolens.core.metrics import count_lines
from repolens.models.file_info import FileInfo

class RepositoryScanner:
    def __init__(self, config: AnalyzerConfig) -> None:
        self.config = config

    def scan(self, root: Path) -> list[FileInfo]:
        files = []
        for path in root.rglob("*"):
            relative = path.relative_to(root)
            if any(part in self.config.ignored_directories for part in relative.parts):
                continue
            if not self.config.include_hidden and any(part.startswith(".") for part in relative.parts):
                continue
            if not path.is_file():
                continue
            try:
                size = path.stat().st_size
            except OSError:
                continue
            language = detect_language(path)
            lines = count_lines(path, size) if language else 0
            files.append(FileInfo(relative, size, language, lines))
        return files
