"""Analyzer configuration."""

from dataclasses import dataclass, field
from repolens.constants import IGNORED_DIRECTORIES

@dataclass(slots=True)
class AnalyzerConfig:
    ignored_directories: set[str] = field(default_factory=lambda: set(IGNORED_DIRECTORIES))
    include_hidden: bool = False
    largest_files_limit: int = 10
