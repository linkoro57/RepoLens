import argparse
from pathlib import Path
from repolens.config import AnalyzerConfig
from repolens.core.analyzer import RepositoryAnalyzer
from repolens.reporting import ConsoleReporter, JsonReporter

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="repolens", description="Analyze repository structure and health.")
    parser.add_argument("path", nargs="?", type=Path, default=Path.cwd(), help="repository to analyze")
    parser.add_argument("--json", type=Path, dest="json_path", help="export the report to JSON")
    parser.add_argument("--include-hidden", action="store_true", help="include hidden files")
    parser.add_argument("--largest", type=int, default=10, help="number of largest files to display")
    return parser

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.path.expanduser().resolve()
    if not root.is_dir():
        print(f"Error: '{root}' is not a valid directory.")
        return 1
    config = AnalyzerConfig(include_hidden=args.include_hidden, largest_files_limit=max(0, args.largest))
    report = RepositoryAnalyzer(config).analyze(root)
    ConsoleReporter().display(report, config.largest_files_limit)
    if args.json_path:
        JsonReporter().write(report, args.json_path.expanduser())
        print(f"\nJSON report written to {args.json_path.expanduser()}")
    return 0
