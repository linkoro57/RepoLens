"""Default analysis rules."""

LANGUAGES = {
    ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
    ".jsx": "JavaScript", ".tsx": "TypeScript", ".lua": "Lua",
    ".luau": "Luau", ".html": "HTML", ".css": "CSS", ".scss": "SCSS",
    ".java": "Java", ".c": "C", ".h": "C", ".cpp": "C++",
    ".hpp": "C++", ".cs": "C#", ".go": "Go", ".rs": "Rust",
    ".php": "PHP", ".rb": "Ruby", ".swift": "Swift", ".kt": "Kotlin",
    ".sh": "Shell", ".ps1": "PowerShell", ".sql": "SQL",
    ".json": "JSON", ".yaml": "YAML", ".yml": "YAML", ".toml": "TOML",
    ".md": "Markdown", ".xml": "XML",
}

IGNORED_DIRECTORIES = frozenset({
    ".git", ".hg", ".svn", ".idea", ".vscode", ".venv", "venv",
    "env", "node_modules", "dist", "build", "coverage", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", "__pycache__",
})

JUNK_NAMES = frozenset({
    ".DS_Store", "Thumbs.db", "desktop.ini", ".coverage",
})

JUNK_SUFFIXES = frozenset({".pyc", ".pyo", ".tmp", ".bak", ".log"})
MAX_TEXT_BYTES = 2_000_000
