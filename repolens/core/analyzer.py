from pathlib import Path
from repolens.config import AnalyzerConfig
from repolens.core.diagnostics import diagnose
from repolens.core.scanner import RepositoryScanner
from repolens.core.scoring import calculate_score
from repolens.models.report import AnalysisReport

class RepositoryAnalyzer:
    def __init__(self, config: AnalyzerConfig | None = None) -> None:
        self.config = config or AnalyzerConfig()

    def analyze(self, root: Path) -> AnalysisReport:
        root = root.expanduser().resolve()
        files = RepositoryScanner(self.config).scan(root)
        languages: dict[str, int] = {}
        for item in files:
            if item.language:
                languages[item.language] = languages.get(item.language, 0) + item.lines
        issues = diagnose(root, files)
        return AnalysisReport(
            root=root, files=files, issues=issues, languages=languages,
            total_lines=sum(item.lines for item in files),
            total_size=sum(item.size for item in files),
            score=calculate_score(issues),
        )
