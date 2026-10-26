from pathlib import Path
from repolens.constants import LANGUAGES

def detect_language(path: Path) -> str | None:
    return LANGUAGES.get(path.suffix.lower())
