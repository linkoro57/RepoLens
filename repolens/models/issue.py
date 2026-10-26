from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class Issue:
    code: str
    message: str
    path: Path | None = None
    penalty: int = 0
