import os
import shutil
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# ------------------------------------------------------
# Configuration
# ------------------------------------------------------

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
BUILD_DIR = BASE_DIR / "build"
DATA_DIR = BASE_DIR / "data"
CATEGORIES_FILE = DATA_DIR / "categories.json"

# ------------------------------------------------------
# Load categories
# ------------------------------------------------------

def load_categories():
    if not CATEGORIES_FILE.exists():
        return {}
    with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

CATEGORIES = load_categories()

# ------------------------------------------------------
# Setup Jinja2 environment
# ------------------------------------------------------

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=True
)

# ------------------------------------------------------
# Helper to render and save a page
# ------------------------------------------------------

def render_page(template_name, output_path, context=None):
    if context is None:
        context = {}
    template = env.get_template(template_name)
    html = template.render(**context)
    output_file = BUILD_DIR / output_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(html, encoding="utf-8")
    print(f"✅ Rendered: {output_path}")

# ------------------------------------------------------
# Build all pages
# ------------------------------------------------------

def build():
    # 1. Clean build directory
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)

    # 2. Copy static files
    shutil.copytree(STATIC_DIR, BUILD_DIR / "static")
    print("📦 Copied static files")

    # 3. Render pages
    # Home
    render_page("home/index.html", "index.html", {"request": {}})

    # Shop
    render_page("shop/shop.html", "shop/index.html", {"request": {}})

    # About
    render_page("about/about.html", "about/index.html", {"request": {}})

    # Contact
    render_page("contact/contact.html", "contact/index.html", {"request": {}})

    # Category pages (6)
    for slug, category in CATEGORIES.items():
        context = {
            "request": {},
            "category": category,
            "slug": slug
        }
        render_page(
            "category/category_detail.html",
            f"category/{slug}/index.html",
            context
        )

    print(f"🎉 Build complete! Output in: {BUILD_DIR}")

if __name__ == "__main__":
    build()