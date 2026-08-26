from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from pathlib import Path

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(title="GiftAura+")

# =====================================================
# Static Files
# =====================================================

app.mount("/static", StaticFiles(directory="static"), name="static")

# =====================================================
# Templates
# =====================================================

templates = Jinja2Templates(directory="templates")

# =====================================================
# Load Category Data from JSON
# =====================================================

DATA_DIR = Path(__file__).parent / "data"
CATEGORIES_FILE = DATA_DIR / "categories.json"

def load_categories():
    if not CATEGORIES_FILE.exists():
        return {}
    with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

CATEGORIES = load_categories()

# =====================================================
# Routes
# =====================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home/index.html"
    )

@app.get("/shop", response_class=HTMLResponse)
async def shop(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="shop/shop.html"
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about/about.html"
    )

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact/contact.html"
    )

# =====================================================
# Category Detail Page (dynamic)
# =====================================================

@app.get("/category/{slug}", response_class=HTMLResponse)
async def category_detail(request: Request, slug: str):
    category = CATEGORIES.get(slug)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return templates.TemplateResponse(
        request=request,
        name="category/category_detail.html",
        context={"request": request, "category": category, "slug": slug}
    )