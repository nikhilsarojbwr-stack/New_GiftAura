# GiftAura Image Guide

This guide explains where images live, how the pages connect them, and how to add or replace images later.

## 1. How image URLs work

FastAPI serves the `static` folder with this mount in `main.py`:

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

Because of this mapping:

| File on disk | URL used by HTML |
|---|---|
| `static/images/home-hero-banner.jpg` | `/static/images/home-hero-banner.jpg` |
| `static/images/celebrations/birthday.webp` | `/static/images/celebrations/birthday.webp` |
| `static/images/products/example.png` | `/static/images/products/example.png` |

Use forward slashes in URLs, including on Windows. Use an absolute URL beginning with `/static/` in templates. For example:

```html
<img src="/static/images/hero-event-scene.webp" alt="Celebration setup">
```

Do not use Windows paths such as `static\\images\\file.png` in HTML.

## Quick reference: where to edit an image

| Image you want to change | Edit this file | Search for this text |
|---|---|---|
| Home hero banner | `templates/shared/base.html` | `--img-home-hero-banner` |
| About hero background | `templates/shared/base.html` | `--img-home-hero-banner` |
| About event scene | `templates/about/about.html` | `hero-event-scene.webp` |
| About founder photo | `templates/about/about.html` | `vidhi.webp` or `nikhil.webp` |
| About timeline image | `templates/about/about.html` | `timeline-01.webp` through `timeline-05.webp` |
| About CTA image | `templates/about/about.html` | `cta-event-family.webp` |
| Category hero image | `data/categories.json` | the category's `"image"` value |
| Category gallery image | `data/categories.json` | the category's `"gallery"` list |
| Category final CTA banner | `templates/shared/base.html` | `--img-banner` |
| Home celebration card | `templates/components/category_section.html` | the relevant `<img src>` |
| Product card image | product data or `product.image` source | `product.image` |

The shared image variables are now written in the HTML body in
`templates/shared/base.html`. CSS still reads these variables for backgrounds,
but the image URL is no longer loaded from `static/css/images.css`.

Example: to replace the home hero, change only the URL after
`--img-home-hero-banner`:

```html
--img-home-hero-banner: url('/static/images/my-new-home-hero.webp');
```

Put the new file at `static/images/my-new-home-hero.webp` first.

## 2. Image folders

```text
static/images/
  home-hero-banner.jpg       Home and shared hero banner
  hero-event-scene.webp      About page hero or event scene
  cta-event-family.webp      Category page final call-to-action banner
  branch-left.png            Decorative about-page branch
  timeline-01.webp           About-page timeline image
  timeline-02.webp
  timeline-03.webp
  timeline-04.webp
  timeline-05.webp
  celebrations/
    birthday.webp
    anniversary.webp
    romantic.webp
    proposal.webp
    cafe.webp
    custom.webp
    birthday-gallery1.webp
    birthday-gallery2.webp
    birthday-gallery3.webp
    anniversary-gallery1.webp
    anniversary-gallery2.webp
  products/                   Product assets
```

Keep related images in the matching folder. Use lowercase names with hyphens or the existing naming pattern. Prefer `.webp` for new photographic images when possible, with `.jpg` or `.png` as fallbacks when needed.

## 3. Where each page gets its images

### Home page

File: `templates/home/index.html`

The home page includes reusable components. The main hero is included from:

```jinja2
{% include 'components/hero.html' %}
```

The hero markup is in `templates/components/hero.html`. Product, category, occasion, testimonial, and form sections are separate files in `templates/components/`.

### Home hero

File: `templates/components/hero.html`

The hero section has the class `.ga-home-hero`. Its visual appearance is controlled mainly by `static/css/about.css`, because that stylesheet contains the shared home/about hero rules.

The stylesheet reads this CSS variable:

```css
var(--img-home-hero-banner)
```

The variable is defined in the HTML body in `templates/shared/base.html`:

```html
<body style="
    --img-home-hero-banner: url('/static/images/home-hero-banner.jpg');
">
```

Keep the existing CSS unchanged. It uses `var(--img-home-hero-banner)` as the
background image and applies the existing gradient, crop, and responsive rules.

### About page

File: `templates/about/about.html`

The About hero uses `.ga-about-hero`. The page also contains direct image tags for the event scene, founders, timeline, stories, and final CTA images.

The existing event scene connection is:

```html
<img src="/static/images/hero-event-scene.webp" alt="Elegant GiftAura celebration setup">
```

The shared hero styling is in `static/css/about.css`. Check whether the image is being displayed as an HTML image or as a CSS background before changing it. The rule `.ga-hero-visual { display: none; }` can hide an image placed inside `.ga-hero-visual`.

### Category detail pages

File: `templates/category/category_detail.html`

Category pages are dynamic. The route loads a category from `data/categories.json` and sends it to the template:

```python
category = CATEGORIES.get(slug)
```

The hero image is supplied by the JSON value `category.image`:

```jinja2
<img src="{{ category.image }}" alt="{{ category.title }}">
```

The category image is therefore edited in `data/categories.json`, not normally in the HTML template.

The category final CTA banner is near the bottom of the same template. Its CSS
variable is set in `templates/shared/base.html`:

```html
--img-banner: url('/static/images/cta-event-family.webp');
```

### Celebration category cards

File: `templates/components/category_section.html`

These cards use direct paths:

```html
<img src="/static/images/celebrations/birthday.webp" alt="Birthday decoration setup">
```

The wrapper class, such as `.birthday-visual`, controls the card background and `.category-visual img` controls the actual image sizing. The HTML `<img>` is the preferred source; do not add a second CSS background unless it is deliberately needed as a fallback.

### Shop products

Product pages use Jinja values:

```jinja2
<img src="{{ product.image }}" alt="{{ product.title }}">
```

The value of `product.image` must already be a browser URL such as `/static/images/products/item.webp`. The CSS only controls layout; it does not find the file.

The older hard-coded best seller component contains one relative Windows-style path and several inline SVG data URLs. For new real images, use `/static/images/...` instead of either pattern.

## 4. What CSS does

HTML chooses the image file. CSS controls how that file looks on the page.

| CSS selector | Controls |
|---|---|
| `.hero-visual img` | Category hero image size and crop |
| `.category-visual img` | Celebration card image size and crop |
| `.service-image img` | Category service image size and crop |
| `.gallery-card img` | Category gallery image size and hover zoom |
| `.occasion-card img` | Occasion icon/image size |
| `.product-card img` | Product card image layout |
| `.ga-hero-background` | Full-bleed home/about hero image layer |
| `.final-cta-background` | Full-bleed category CTA image layer |

Common rules:

```css
img {
    max-width: 100%;
    display: block;
}

.category-visual img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

`object-fit: cover` fills the box and may crop the edges. Use `object-fit: contain` when the complete product must remain visible.

For a full-bleed background image, the parent needs `position: relative`, the image needs absolute positioning, and the text needs a higher `z-index`:

```css
.image-section {
    position: relative;
    overflow: hidden;
}

.image-section > img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.image-section .content {
    position: relative;
    z-index: 1;
}
```

## 5. How to add a new image

1. Copy the file into the correct folder under `static/images/`.
2. Give it a clear lowercase name, for example `birthday-table-setup.webp`.
3. Add the URL with `/static/` in the relevant HTML or JSON file.
4. Add useful alt text that describes the image.
5. Check the CSS selector for the image container and confirm its aspect ratio, height, and `object-fit`.
6. Open the relevant route and check desktop and mobile sizes.

Example for a new category gallery image:

```json
"gallery": [
  "/static/images/celebrations/birthday-table-setup.webp"
]
```

Example for a direct template image:

```html
<img
    src="/static/images/celebrations/birthday-table-setup.webp"
    alt="Birthday table decoration setup"
    loading="lazy"
>
```

## 6. How to replace an image

Keep the URL and replace the file if the new image has the same purpose and filename. This changes the image without changing templates.

If the new image has a different filename:

1. Update the `src` in the template or the value in `categories.json`.
2. Search the workspace for the old filename.
3. Update every reference found.
4. Confirm the new file exists under `static/images/`.

Useful searches:

```text
home-hero-banner
hero-event-scene
cta-event-family
/static/images/
category.image
product.image
```

## 7. Troubleshooting checklist

### Broken image icon

- Confirm the file exists under `static/images/`.
- Confirm the URL starts with `/static/`.
- Check spelling and file extension.
- Use forward slashes.
- Open the image URL directly, for example `http://127.0.0.1:8000/static/images/hero-event-scene.webp`.

### Image URL returns 404

The browser URL does not match the file path. Compare the URL after `/static/` with the path inside the `static` folder.

### Image exists but is not visible

- Inspect whether the image or its parent has `display: none`.
- Check that the parent has a height or aspect ratio.
- Check `z-index` when text overlays the image.
- Check whether a CSS `background-image` uses an undefined variable.
- Remember that an empty `src` or missing Jinja value renders no useful image.

### Image looks stretched

Use a fixed container with `object-fit: cover` or `contain`. Do not force both width and height on an image without setting `object-fit`.

## 8. Recommended rule for future work

Keep image file selection in HTML or JSON and keep sizing, cropping, overlays, and responsive behavior in CSS. This makes image replacement simple and prevents an image from disappearing when a CSS variable is removed.
