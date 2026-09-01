GiftAura About Us — reference implementation

Files:
- templates/about.html
- static/css/about.css
- static/images/*

The image assets are crops from the supplied reference screenshot so the page
uses the same visible photo content. Because the source reference itself is
864px wide, these assets are best viewed near the reference scale.

Add to your base template's <head>:
<link rel="stylesheet" href="/static/css/about.css">

The page expects your existing shared/base.html and your Flask/Jinja static
directory structure.
