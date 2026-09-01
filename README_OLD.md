Your polished README is below.

# 🎁 GiftAura+ – Premium Customized Gifts E-Commerce Platform

**GiftAura+** is a modern, fully responsive e-commerce web application for discovering and ordering handcrafted, personalized gifts for every occasion. Built with **FastAPI**, **Jinja2**, and modern frontend technologies, the project demonstrates enterprise-grade component-based architecture, responsive design, and elegant user experience.

**Last Updated:** 2026-09-01  
**Version:** 1.0.0+  
**Status:** Production-Ready  

---

## 📊 Project Overview

GiftAura+ is an end-to-end gift e-commerce platform that bridges the gap between gift seekers and custom gift creators. The application serves multiple user flows:

1. **Browse & Discover** – Users explore curated gift categories and occasions
2. **Search & Filter** – Dynamic product discovery through search functionality
3. **Personalize** – "Design Your Dream Gift" form for custom requests
4. **Engage** – Newsletter subscriptions and customer testimonials
5. **Purchase Intent** – Shopping cart and wishlist UI framework

---

## ✨ Key Features

### Frontend Features
* 🎯 **Hero Section** – Eye-catching landing with call-to-action buttons
* 🛍️ **Best Sellers Showcase** – Featured products with product cards
* ❤️ **Wishlist & Cart UI** – Frontend framework for e-commerce workflow
* 🔍 **Smart Search Bar** – Product search functionality
* 🎁 **Category Navigation** – Shop by gift category (Birthdays, Anniversaries, etc.)
* 🎉 **Occasion-Based Shopping** – Shop by celebration type
* ✍️ **Dream Gift Form** – Custom gift request submission
* ⭐ **Social Proof** – Customer testimonials section
* ❓ **FAQ Accordion** – Interactive FAQ with collapsible items
* 🚚 **Trust Indicators** – Feature highlights and trust bar
* 📧 **Newsletter Signup** – Email subscription component
* 🧩 **Reusable Components** – Modular Jinja2 template architecture

### Technical Features
* 📱 **Fully Responsive Design** – Mobile-first, works on all devices
* ⚡ **Component-Based Templates** – DRY principle with Jinja2 reusable components
* 🗂️ **Dynamic Routing** – Category pages with URL slugs
* 📦 **Static Asset Management** – Optimized CSS, JS, and image serving
* 🔗 **Modular Architecture** – Easy to extend and maintain
* 🚀 **Production-Ready** – Docker support with Dockerfile included

---

## 🛠️ Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Backend Framework** | FastAPI | 0.141.1 |
| **ASGI Server** | Uvicorn | 0.52.0 |
| **Template Engine** | Jinja2 | 3.1.6 |
| **Data Format** | JSON | — |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) | ES6+ |
| **Language** | Python | 3.10+ |
| **Database** (Optional) | MongoDB | 4.17.0 |
| **Production Server** | Gunicorn + Uvicorn | — |
| **Containerization** | Docker | — |

---

## 📁 Detailed Project Structure

```
gap/
├── main.py                          # FastAPI application entry point
├── build.py                         # Build utilities
├── dev_tools.py                     # Development tools
├── flow.md                          # Project flow documentation
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker configuration
├── .gitignore                       # Git ignore rules
├── .dockerignore                    # Docker ignore rules
├── push_giftaura.bat                # Deployment batch script
├── README.md                        # This file
├── PROJECT_STRUCTURE.md             # Auto-generated structure
│
├── data/                            # Application data
│   └── categories.json              # Category definitions & metadata
│
├── static/                          # Static assets (served by FastAPI)
│   ├── css/                         # Stylesheets
│   │   ├── style.css                # Main stylesheet (global styles)
│   │   ├── about.css                # About page specific styles
│   │   └── s.css                    # Secondary/utility styles
│   ├── images/                      # Image assets
│   │   ├── celebrations/            # Occasion-specific images
│   │   │   ├── anniversary.webp
│   │   │   ├── anniversary-gallery[1-2].webp
│   │   │   ├── birthday.webp
│   │   │   ├── birthday-gallery[1-3].webp
│   │   │   ├── cafe.webp
│   │   │   ├── custom.webp
│   │   │   ├── proposal.webp
│   │   │   └── romantic.webp
│   │   ├── products/                # Product images
│   │   │   ├── [product-id].png     # Product photos
│   │   │   └── ...
│   │   ├── brand-left.png
│   │   ├── branch-left.png
│   │   ├── cta-event-family.webp
│   │   ├── hero-event-scene.webp
│   │   ├── timeline-[01-05].webp    # Timeline/process images
│   │   └── [testimonial-images]
│   └── js/                          # JavaScript files
│
├── templates/                       # Jinja2 templates (server-side rendering)
│   ├── __init__.py                  # Template package marker
│   ├── base.html                    # NOT HERE - see shared/
│   │
│   ├── shared/                      # Shared layout components
│   │   ├── base.html                # Master template (layout, meta tags)
│   │   ├── navbar.html              # Navigation bar component
│   │   └── footer.html              # Footer component
│   │
│   ├── components/                  # Reusable UI components
│   │   ├── hero.html                # Hero section (CTA)
│   │   ├── best_sellers_section.html# Best sellers product grid
│   │   ├── product_card.html        # Individual product card template
│   │   ├── category_section.html    # Category showcase section
│   │   ├── occasion_section.html    # Occasion-based shopping section
│   │   ├── search_bar.html          # Product search input
│   │   ├── dream_gift_form.html     # Custom gift request form
│   │   ├── testimonials_section.html# Customer reviews/testimonials
│   │   ├── faq.html                 # FAQ accordion component
│   │   ├── newsletter.html          # Email signup component
│   │   ├── trust_bar.html           # Trust indicators/badges
│   │   ├── feature_card.html        # Feature highlight cards
│   │   ├── why_choose.html          # Value proposition section
│   │   ├── breadcrumb.html          # Breadcrumb navigation
│   │   └── pagination.html          # Pagination component
│   │
│   ├── home/                        # Home page templates
│   │   └── index.html               # Home page (imports components)
│   │
│   ├── shop/                        # Shop/catalog templates
│   │   └── shop.html                # Shop listing page
│   │
│   ├── category/                    # Category detail pages
│   │   └── category_detail.html     # Dynamic category page
│   │
│   ├── product/                     # Product detail templates
│   │   └── product_details.html     # Individual product page
│   │
│   ├── about/                       # About page templates
│   │   └── about.html               # Company/brand info page
│   │
│   ├── contact/                     # Contact page templates
│   │   └── contact.html             # Contact form & info page
│   │
│   └── faq.html                     # Standalone FAQ page
```

---

## 🔌 API Endpoints & Routing

GiftAura+ provides the following HTTP endpoints (FastAPI routes):

### Page Routes (GET)
| Endpoint | Template | Purpose |
|----------|----------|---------|
| `/` | `home/index.html` | Landing/Home page |
| `/shop` | `shop/shop.html` | Product catalog/shop |
| `/about` | `about/about.html` | About company page |
| `/contact` | `contact/contact.html` | Contact & support page |
| `/category/<slug>` | `category/category_detail.html` | Dynamic category detail page |

### Data Structure
- **Categories**: Loaded from `data/categories.json`
- **Dynamic Routing**: Category slugs map to category objects stored in JSON

---

## 📊 Data Flow & Architecture

### Request-Response Flow
```
User Browser
    ↓
FastAPI Route Handler (@app.get)
    ↓
Load Data (categories.json)
    ↓
Jinja2 Template Rendering
    ↓
Include Components (hero, products, etc.)
    ↓
HTML Response
    ↓
Static Assets (CSS/JS/Images)
    ↓
Browser Rendering
```

### Component Hierarchy
```
base.html (Master Layout)
├── navbar.html
├── [Page-specific content via @app.get route]
│   ├── hero.html
│   ├── best_sellers_section.html
│   │   └── product_card.html (repeated)
│   ├── category_section.html
│   ├── occasion_section.html
│   ├── search_bar.html
│   ├── dream_gift_form.html
│   ├── testimonials_section.html
│   │   └── testimonial items
│   ├── faq.html
│   │   └── FAQ accordion items
│   ├── newsletter.html
│   ├── trust_bar.html
│   └── why_choose.html
│       └── feature_card.html (repeated)
└── footer.html
```

---

## 📝 Categories Data Structure

The `data/categories.json` file contains category definitions. Example structure:
```json
{
  "birthday": {
    "name": "Birthday Gifts",
    "slug": "birthday",
    "description": "Perfect gifts for birthdays",
    "image": "/static/images/celebrations/birthday.webp"
  },
  "anniversary": {
    "name": "Anniversary Gifts",
    "slug": "anniversary",
    "description": "Celebrate special moments",
    "image": "/static/images/celebrations/anniversary.webp"
  }
}
```

When a user visits `/category/birthday`, the route handler:
1. Retrieves the category from JSON
2. Passes it to the template context
3. Renders `category/category_detail.html` with category data

---

## 🧩 Template & Component System

### Shared Templates (Layout)
- **base.html**: Master layout with meta tags, head, and body structure
- **navbar.html**: Responsive navigation bar
- **footer.html**: Site footer with links and info

### Page Templates
- **home/index.html**: Home page - imports components in specific order
- **shop/shop.html**: Shopping catalog/listing view
- **category/category_detail.html**: Dynamic category display (receives category context)
- **product/product_details.html**: Individual product detail page
- **about/about.html**: About/company information
- **contact/contact.html**: Contact form and info

### Reusable Components
All components in `templates/components/` are included via Jinja2 `{% include %}` tags:
- **hero.html**: Call-to-action banner
- **best_sellers_section.html**: Featured products grid
- **product_card.html**: Individual product card (reused multiple times)
- **category_section.html**: Category showcase
- **occasion_section.html**: Occasion-based shopping
- **search_bar.html**: Search functionality UI
- **dream_gift_form.html**: Custom order form
- **testimonials_section.html**: Customer reviews
- **faq.html**: FAQ accordion
- **newsletter.html**: Email signup
- **trust_bar.html**: Trust badges/features
- **feature_card.html**: Feature highlight
- **why_choose.html**: Value proposition
- **breadcrumb.html**: Navigation trail
- **pagination.html**: Page navigation

---

## 🎨 Styling Architecture

### CSS Organization
- **style.css**: Global styles, typography, colors, layout
- **about.css**: About page specific overrides
- **s.css**: Secondary/utility styles

### Styling Approach
- Mobile-first responsive design
- CSS Grid and Flexbox for layouts
- Google Fonts integration
- CSS Custom Properties (variables) for theming

---

## 📦 Dependencies

### Core Dependencies
- **fastapi** (0.141.1) – Web framework
- **uvicorn** (0.52.0) – ASGI server
- **jinja2** (3.1.6) – Template engine
- **starlette** (1.3.1) – HTTP utilities

### Optional Dependencies
- **pymongo** (4.17.0) – MongoDB driver (for future database integration)
- **python-dotenv** (1.2.2) – Environment configuration
- **pydantic** (2.13.4) – Data validation

For complete list, see [requirements.txt](requirements.txt)

---

## 🚀 How to Run

### Prerequisites
- Python 3.10+
- pip or conda
- Virtual environment (recommended)

### Quick Start

---

# 📋 Prerequisites

Before running this project, ensure you have the following installed:

* Python **3.10 or newer**
* Git
* pip

Verify your installation:

```bash
python --version
git --version
pip --version
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/nikhilsarojbwr-stack/GiftAura.git
```

Move into the project directory:

```bash
cd GiftAura
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
uvicorn main:app --reload
```

You should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 5. Open Your Browser

Visit:

```
http://127.0.0.1:8000
```

The GiftAura homepage should now be running locally.

---

# 🧩 How It Works

GiftAura follows a modular component architecture.

* **FastAPI** handles routing and serves the application.
* **Jinja2** renders reusable HTML components.
* **base.html** provides the shared layout.
* Individual sections (Hero, Categories, FAQ, Testimonials, etc.) are stored inside the `templates/components/` directory.
* Static assets (CSS, JavaScript, Images) are served from the `static/` directory.

This architecture keeps templates reusable, maintainable, and easy to extend.

---

# 🎨 Customization

## Styling

Modify:

```text
static/css/style.css
```

to customize:

* Colors
* Typography
* Layout
* Buttons
* Cards
* Animations
* Spacing

---

## Content

Replace the placeholder content with your own:

* Products
* Categories
* Testimonials
* FAQ
* Images
* Brand Information

---

## Forms

The "Design Your Dream Gift" form can easily be connected to:

* Database
* Email Service
* REST API
* CRM
* ERP

---

# 📦 Deployment

Run the production server using:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

For production environments, consider:

* Docker
* Render
* Railway
* Azure App Service
* AWS EC2
* DigitalOcean
* Nginx + Gunicorn + Uvicorn

Example:

```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/my-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature/my-feature
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it according to the license terms.

---

# 🙌 Acknowledgments

* FastAPI
* Jinja2
* Google Fonts
* Open Source Community

Special thanks to everyone who contributes to open-source software.

---

# 👨‍💻 Author

**Nikhil Saroj**

GitHub:

[https://github.com/nikhilsarojbwr-stack](https://github.com/nikhilsarojbwr-stack)

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 🐛 Report issues
* 💡 Suggest improvements
* 🤝 Contribute to the project

Your support is greatly appreciated.

---

# 📬 Contact

If you have any questions or suggestions, feel free to open an issue or submit a pull request.

---

## 🌟 GiftAura

> **Every Gift Becomes A Beautiful Memory.**

# 🎁 GiftAura – Premium Customized Gifts

**GiftAura** is a modern, fully responsive e‑commerce website that offers **handcrafted, personalized gifts** for every occasion. The platform allows users to browse best‑selling products, shop by category or occasion, and submit a custom gift request – all within a beautifully designed interface.

---

## ✨ Features

- **Hero Section** – Engaging headline, call‑to‑action buttons, and a trust bar highlighting key benefits.
- **Best Sellers Carousel** – Showcases top products with “bestseller” badges, wishlist icons, and quick‑view hover actions.
- **Shop by Category** – Visual grid with overlays for gift categories (For Her, For Him, Couples, etc.).
- **Shop by Occasion** – Icon‑based cards for Birthday, Anniversary, Valentine’s, Christmas, etc.
- **Design Your Dream Gift** – A custom order form with fields for name, email, occasion, delivery date, and file upload.
- **Why Choose Us** – Feature grid highlighting core values (handmade, personalised, free shipping, 24/7 support).
- **Customer Testimonials** – Scrollable cards with real reviews and star ratings.
- **FAQ Accordion** – Clean, two‑column list of frequently asked questions.
- **Responsive Navigation** – Sticky header with search bar, wishlist, cart badge, and mobile hamburger menu.
- **Footer** – Brand info, quick links, customer service, newsletter signup, and social icons.

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend**: HTML5, CSS3 (custom), JavaScript (vanilla)
- **Templating**: [Jinja2](https://jinja.palletsprojects.com/)
- **Fonts**: Google Fonts (Playfair Display, Poppins, Great Vibes)
- **Icons**: Embedded SVG & Unicode symbols

---

## 📁 Project Structure

```
gap/
├── static/
│   ├── css/
│   │   └── style.css          # All global styles
│   ├── images/                # (optional) product/avatar images
│   └── js/                    # (optional) external JavaScript
├── templates/
│   ├── about/
│   │   └── about.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   ├── components/
│   │   ├── best_sellers_section.html
│   │   ├── breadcrumb.html
│   │   ├── category_card.html
│   │   ├── category_section.html
│   │   ├── dream_gift_form.html
│   │   ├── faq.html
│   │   ├── feature_card.html
│   │   ├── hero.html
│   │   ├── newsletter.html
│   │   ├── occasion_card.html
│   │   ├── occasion_section.html
│   │   ├── pagination.html
│   │   ├── product_card.html
│   │   ├── search_bar.html
│   │   ├── testimonial_card.html
│   │   ├── testimonials_section.html
│   │   ├── trust_bar.html
│   │   └── why_choose.html
│   ├── contact/
│   │   └── contact.html
│   ├── home/
│   │   └── index.html         # Homepage (includes all sections)
│   ├── product/
│   │   └── product_details.html
│   ├── shared/
│   │   ├── base.html          # Main layout with navbar, footer, scripts
│   │   ├── footer.html
│   │   └── navbar.html
│   └── shop/
│       └── shop.html
├── .gitignore
├── main.py                     # FastAPI application entry point
├── requirements.txt
├── README.md
└── PROJECT_STRUCTURE.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone(https://github.com/nikhilsarojbwr-stack/GiftAura)
cd gap
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Open your browser

Visit [http://localhost:8000](http://localhost:8000) – you should see the GiftAura homepage.

---

## 🧩 How It Works

- **Templates** are rendered using **Jinja2** with a modular component approach.
- Each section (Hero, Best Sellers, Categories, etc.) lives in its own file under `templates/components/`.
- The `base.html` provides the common layout (navbar, footer, styles, scripts).
- All static assets (CSS, images, JS) are served from the `/static` folder.
- The homepage (`index.html`) simply includes all section components – making it clean and easy to maintain.

---

## 🧪 Customisation

- **Styles**: All CSS variables are defined in `static/css/style.css` – you can easily change colours, fonts, spacing, etc.
- **Content**: Replace static product cards, category items, testimonials, and FAQ entries with your own data (or connect to a database).
- **Forms**: The “Design Your Dream Gift” form currently shows an alert on submit; you can connect it to an email endpoint or a database.

---

## 📦 Deployment

For production deployment:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

<img width="1193" height="921" alt="image" src="https://github.com/user-attachments/assets/1d2140f5-8a63-4cc4-9b40-6edb7fb06269" />

<img width="1196" height="784" alt="image" src="https://github.com/user-attachments/assets/6832d3f6-9ba8-40d5-8a2e-920249cf5c89" />

<img width="1188" height="959" alt="image" src="https://github.com/user-attachments/assets/6b841e22-07a6-474b-a8bc-e44b0eb5dfab" />

<img width="1191" height="935" alt="image" src="https://github.com/user-attachments/assets/41d9eb81-bd25-4bb9-8034-e99a08bdcca3" />

<img width="1192" height="797" alt="image" src="https://github.com/user-attachments/assets/c4717e53-cb50-4a4c-bc32-3b3ad6dc4e59" />

<img width="1204" height="973" alt="image" src="https://github.com/user-attachments/assets/cd4e1fcc-3f56-4201-9832-80f103063917" />


Consider using `gunicorn` with `uvicorn.workers.UvicornWorker` for better concurrency, or deploy on platforms like **Render**, **Heroku**, or **AWS**.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- Built with ❤️ using FastAPI and Jinja2.
- Design inspired by modern gift‑shop aesthetics.
- Special thanks to all the open‑source libraries that made this possible.

---

**GiftAura** – *Every Gift Becomes A Beautiful Memory* ✦
