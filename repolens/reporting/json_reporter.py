import json
from pathlib import Path
from repolens.models.report import AnalysisReport

class JsonReporter:
    def write(self, report: AnalysisReport, destination: Path) -> None:
        payload = {
            "root": str(report.root), "score": report.score,
            "files": len(report.files), "lines": report.total_lines,
            "size_bytes": report.total_size, "main_language": report.main_language,
            "languages": report.languages,
            "largest_files": [
                {"path": str(item.path), "size": item.size, "lines": item.lines}
                for item in sorted(report.files, key=lambda file: file.size, reverse=True)[:10]
            ],
            "issues": [
                {"code": issue.code, "message": issue.message, "path": str(issue.path) if issue.path else None}
                for issue in report.issues
            ],
        }
        destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")
