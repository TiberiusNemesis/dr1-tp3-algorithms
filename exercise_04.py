"""Exercise 4: recursive directory traversal."""

from pathlib import Path
from tempfile import TemporaryDirectory

# Exercise 4: recursively traverse direct directory entries.
def walk_directory(root: str | Path) -> list[str]:
    """Return a sorted, indented listing without following symlinks."""
    root_path = Path(root)
    if not root_path.exists():
        raise FileNotFoundError(root_path)
    if root_path.is_file() or root_path.is_symlink():
        return [root_path.name]

    lines: list[str] = []

    def visit(directory: Path, depth: int) -> None:
        for entry in sorted(directory.iterdir(), key=lambda item: item.name):
            prefix = "  " * depth
            if entry.is_symlink():
                lines.append(f"{prefix}{entry.name} [symlink]")
            elif entry.is_dir():
                lines.append(f"{prefix}{entry.name}/")
                visit(entry, depth + 1)
            else:
                lines.append(f"{prefix}{entry.name}")

    visit(root_path, 0)
    return lines


if __name__ == "__main__":
    with TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "alpha.txt").write_text("top-level file", encoding="utf-8")
        (root / "empty").mkdir()
        archive = root / "archive"
        archive.mkdir()
        (archive / "notes.txt").write_text("nested file", encoding="utf-8")
        year = archive / "year"
        year.mkdir()
        (year / "summary.txt").write_text("deep file", encoding="utf-8")
        print("\n".join(walk_directory(root)))
