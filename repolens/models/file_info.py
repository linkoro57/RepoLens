from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class FileInfo:
    path: Path
    size: int
    language: str | None
    lines: int
