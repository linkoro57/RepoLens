from pathlib import Path
from repolens.constants import JUNK_NAMES, JUNK_SUFFIXES
from repolens.models.file_info import FileInfo
from repolens.models.issue import Issue

def diagnose(root: Path, files: list[FileInfo]) -> list[Issue]:
    issues = []
    if not (root / "README.md").exists():
        issues.append(Issue("missing-readme", "Repository has no README.md", penalty=12))
    if not any((root / name).exists() for name in ("LICENSE", "LICENSE.md", "LICENSE.txt")):
        issues.append(Issue("missing-license", "Repository has no license file", penalty=8))
    if not (root / ".gitignore").exists():
        issues.append(Issue("missing-gitignore", "Repository has no .gitignore", penalty=6))
    for item in files:
        if item.path.name in JUNK_NAMES or item.path.suffix.lower() in JUNK_SUFFIXES:
            issues.append(Issue("junk-file", "Generated or unnecessary file detected", item.path, 2))
        if item.size > 5_000_000:
            issues.append(Issue("large-file", "File is larger than 5 MB", item.path, 3))
    return issues
