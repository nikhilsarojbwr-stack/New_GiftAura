from pathlib import Path
from datetime import datetime

# ==========================================================
# Configuration
# ==========================================================

PROJECT_ROOT = Path(__file__).parent
OUTPUT_FILE = PROJECT_ROOT / "PROJECT_STRUCTURE.md"

IGNORE_FOLDERS = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    ".pytest_cache",
    ".venv",
}

IGNORE_FILES = {
    # e.g. "secret.env"
}

# Extensions considered as "data files"
DATA_EXTENSIONS = {
    ".json", ".yaml", ".yml", ".csv", ".txt",
    ".md", ".xml", ".toml", ".ini", ".cfg",
}

# ==========================================================
# Statistics
# ==========================================================

folder_count = 0
file_count = 0
python_file_count = 0
docker_file_count = 0
dockerignore_count = 0
data_file_count = 0

# ==========================================================
# Build Folder Tree
# ==========================================================

def build_tree(folder: Path, prefix: str = ""):
    """
    Recursively builds a folder tree.
    """
    global folder_count, file_count, python_file_count
    global docker_file_count, dockerignore_count, data_file_count

    tree = ""

    items = sorted(
        folder.iterdir(),
        key=lambda x: (x.is_file(), x.name.lower())
    )

    items = [
        item for item in items
        if item.name not in IGNORE_FOLDERS
        and item.name not in IGNORE_FILES
    ]

    total = len(items)

    for index, item in enumerate(items):
        connector = "└── " if index == total - 1 else "├── "
        tree += prefix + connector + item.name + "\n"

        if item.is_dir():
            folder_count += 1
            extension = "    " if index == total - 1 else "│   "
            tree += build_tree(item, prefix + extension)
        else:
            file_count += 1

            # Count Python files
            if item.suffix == ".py":
                python_file_count += 1

            # Count Dockerfiles (case‑insensitive)
            if item.name.lower() == "dockerfile":
                docker_file_count += 1

            # Count .dockerignore
            if item.name == ".dockerignore":
                dockerignore_count += 1

            # Count data files by extension
            if item.suffix in DATA_EXTENSIONS:
                data_file_count += 1

    return tree

# ==========================================================
# Generate Markdown
# ==========================================================

def generate_markdown(tree: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""# GiftAura+ Project Structure

Automatically Generated

Generated On: {now}

---

## Project Structure

```text
{PROJECT_ROOT.name}
{tree}```

## Statistics

- Folders: {folder_count}
- Files: {file_count}
- Python files: {python_file_count}
- Dockerfiles: {docker_file_count}
- .dockerignore files: {dockerignore_count}
- Data files (JSON, YAML, CSV, etc.): {data_file_count}
"""

    return content

def main():
    tree = build_tree(PROJECT_ROOT)
    markdown = generate_markdown(tree)
    OUTPUT_FILE.write_text(markdown, encoding="utf-8")
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()