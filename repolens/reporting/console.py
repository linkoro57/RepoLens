from repolens.core.metrics import format_size
from repolens.models.report import AnalysisReport

class ConsoleReporter:
    def display(self, report: AnalysisReport, largest_limit: int = 10) -> None:
        print(f"\nRepoLens - {report.root}")
        print("=" * 60)
        print(f"Files          {len(report.files)}")
        print(f"Lines          {report.total_lines:,}")
        print(f"Size           {format_size(report.total_size)}")
        print(f"Main language  {report.main_language}")
        print(f"Health score   {report.score}/100")
        if report.languages:
            print("\nLanguages")
            for name, lines in sorted(report.languages.items(), key=lambda pair: pair[1], reverse=True):
                print(f"  {name:<16} {lines:>8,} lines")
        if report.files:
            print("\nLargest files")
            for item in sorted(report.files, key=lambda file: file.size, reverse=True)[:largest_limit]:
                print(f"  {format_size(item.size):>10}  {item.path}")
        if report.issues:
            print("\nIssues")
            for issue in report.issues:
                location = f" ({issue.path})" if issue.path else ""
                print(f"  [{issue.code}] {issue.message}{location}")
