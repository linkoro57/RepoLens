from dataclasses import dataclass, field
from pathlib import Path
from repolens.models.file_info import FileInfo
from repolens.models.issue import Issue

@dataclass(slots=True)
class AnalysisReport:
    root: Path
    files: list[FileInfo] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)
    languages: dict[str, int] = field(default_factory=dict)
    total_lines: int = 0
    total_size: int = 0
    score: int = 100

    @property
    def main_language(self) -> str:
        return max(self.languages, key=self.languages.get) if self.languages else "Unknown"
