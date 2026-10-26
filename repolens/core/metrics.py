from pathlib import Path
from repolens.constants import MAX_TEXT_BYTES

def count_lines(path: Path, size: int) -> int:
    if size > MAX_TEXT_BYTES:
        return 0
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as stream:
            return sum(1 for _ in stream)
    except OSError:
        return 0

def format_size(size: int) -> str:
    value = float(size)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024 or unit == "GB":
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GB"
