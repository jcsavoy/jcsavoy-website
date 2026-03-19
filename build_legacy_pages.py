import os
import re
import shutil

# First, copy the covers to the media directory if they aren't already there
source_covers_dir = "../The Legacy Billionaires/Covers for The Legacy Billionaires"
dest_media_dir = "media/files"

for filename in os.listdir(source_covers_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        shutil.copy2(os.path.join(source_covers_dir, filename), os.path.join(dest_media_dir, filename))

# The template pattern we use for all our book pages
TEMPLATE = """<!DOCTYPE html><html lang="en-us"><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} - JC Savoy website</title><meta name="description" content="{short_blurb}"><meta name="generator" content="Publii Open-Source CMS for Static Site"><link rel="canonical" href="https://jcsavoy.github.io/jcsavoy-website/{filename}"><link rel="alternate" type="application/atom+xml" href="https://jcsavoy.github.io/jcsavoy-website/feed.xml" title="JC Savoy website - RSS"><link rel="alternate" type="application/json" href="https://jcsavoy.github.io/jcsavoy-website/feed.json" title="JC Savoy website - JSON"><meta property="og:title" content="{title}"><meta property="og:site_name" content="JC Savoy website"><meta property="og:description" content="{short_blurb}"><meta property="og:url" content="https://jcsavoy.github.io/jcsavoy-website/{filename}"><meta property="og:type" content="article"><link rel="stylesheet" href="https://jcsavoy.github.io/jcsavoy-website/assets/css/style.css?v=ee2360e8f8095d635b8f0d4cdd7218f9"><link rel="stylesheet" href="assets/css/premium.css"><script type="application/ld+json">{{"@context":"http://schema.org","@type":"Article","mainEntityOfPage":{{"@type":"WebPage","@id":"https://jcsavoy.github.io/jcsavoy-website/{filename}"}},"headline":"{title}","datePublished":"2026-03-15T11:20-04:00","dateModified":"2026-03-19T07:15-04:00","description":"{short_blurb}","author":{{"@type":"Person","name":"JC Savoy","url":"https://jcsavoy.github.io/jcsavoy-website/authors/jc-savoy/"}},"publisher":{{"@type":"Organization","name":"JC Savoy"}}}}</script><noscript><style>img[loading] {{ opacity: 1; }}</style></noscript></head><body class="page-template"><header class="top js-header"><a class="logo" href="https://jcsavoy.github.io/jcsavoy-website/">JC Savoy website</a></header><main class="page"><div class="content"><div class="hero"><div class="hero__content"><div class="wrapper"><h1>{title}</h1></div></div></div><div class="wrapper content__entry content__entry--nospace"><nav id="navbar" style="background-color: #f5f2eb; padding:10px 20px; border-radius:8px; margin-bottom:1rem;"><div class="nav-inner"><a href="./index.html" class="nav-logo" style="color: #000000; font-weight:bold;">JC Savoy</a><ul id="navLinks" class="nav-links" style="display:flex; gap:15px; list-style:none; margin:0; padding:0; align-items:center;"><li><a href="./index.html#about" style="color: #000000; font-weight:500; text-decoration:none;">About</a></li><li><a href="./index.html#series" style="color: #000000; font-weight:500; text-decoration:none;">Series</a></li><li><a href="./index.html#books" style="color: #000000; font-weight:500; text-decoration:none;">Books</a></li><li><a href="./index.html#newsletter" style="color: #000000; font-weight:500; text-decoration:none;">Newsletter</a></li><li><a href="./index.html#connect" style="color: #000000; font-weight:500; text-decoration:none;">Connect</a></li></ul><button id="mobileToggle" class="mobile-toggle" aria-label="Menu"></button></div></nav><div class="wrapper content__entry content__entry--nospace"><section class="book-detail"><div class="book-detail-grid"><div class="book-detail-cover"><figure><img src="media/files/{cover_image}" alt="{title} Cover" data-is-external-image="true"></figure></div><div class="book-detail-info"><p class="book-series-tag">{series_tag}</p><h1 class="book-detail-title">{title}</h1><div class="book-detail-blurb">{blurb_html}</div><div class="book-detail-actions">{buy_button_html}</div></div></div></section></div></div></div></main><footer class="footer"><div class="wrapper"><div class="footer__copyright"></div><button id="backToTop" class="footer__bttop" aria-label="Back to top" title="Back to top"><svg width="20" height="20"><use xlink:href="https://jcsavoy.github.io/jcsavoy-website/assets/svg/svg-map.svg#toparrow"/></svg></button></div></footer><script defer="defer" src="https://jcsavoy.github.io/jcsavoy-website/assets/js/scripts.min.js?v=d0fc1030089a37f93a2d51bf6d07565c"></script><script>window.publiiThemeMenuConfig={{mobileMenuMode:'sidebar',animationSpeed:300,submenuWidth: 'auto',doubleClickTime:500,mobileMenuExpandableSubmenus:true,relatedContainerForOverlayMenuSelector:'.top'}};</script><script>var images = document.querySelectorAll('img[loading]'); for (var i = 0; i < images.length; i++) {{ if (images[i].complete) {{ images[i].classList.add('is-loaded'); }} else {{ images[i].addEventListener('load', function () {{ this.classList.add('is-loaded'); }}, false); }} }}</script></body></html>"""

def get_blurb_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Split text by "Book X:" or "The Legacy... Collection"
    parts = re.split(r"(Book \d+:.*? \n|The Legacy Billionaires Collection.*? \n)", text)
    blurbs = {}
    current_title = None
    
    for part in parts:
        if part.startswith("Book "):
            current_title = part.split(":")[1].strip()
        elif part.startswith("The Legacy Billionaires Collection"):
            current_title = part.strip()
        elif current_title and part.strip():
            blurbs[current_title] = part.strip()
            
    return blurbs

blurbs_dict = get_blurb_text("legacy_blurbs.txt")

books = [
    {
        "id": 1,
        "title": "The Billionaire’s Stand-In Fiancée",
        "slug": "the-billionaires-stand-in-fiancee",
        "cover": "1-B The Billionaire's Stand-In Fiancée.jpg",
        "link": "https://amzn.to/4spg9QA"
    },
    {
        "id": 2,
        "title": "The Billionaire’s Hidden Truth",
        "slug": "the-billionaires-hidden-truth",
        "cover": "2-B The Billionaire's Hidden Truth.jpg",
        "link": "https://amzn.to/4rDLaz6"
    },
    {
        "id": 3,
        "title": "The Billionaire’s Stolen Heart",
        "slug": "the-billionaires-stolen-heart",
        "cover": "3-B The Billionaire's Stolen Heart.jpg",
        "link": "https://amzn.to/3NBPaSy"
    },
    {
        "id": 4,
        "title": "The Billionaire’s Big Heart",
        "slug": "the-billionaires-big-heart",
        "cover": "4-B The Billlionaire's Big Heart.jpg",
        "link": "https://amzn.to/4sUqfJc"
    },
    {
        "id": 5,
        "title": "The Billionaire’s Holiday Second Chance",
        "slug": "the-billionaires-holiday-second-chance",
        "cover": "5-B The Billionaire's Holiday Second Chance.jpg",
        "link": "https://amzn.to/3P9Bsah"
    },
    {
        "id": 6,
        "title": "The Billionaire’s Surprise Son",
        "slug": "the-billionaires-surprise-son",
        "cover": "6-B The Billionaire's Surprise Son with Dino.jpg",
        "link": "https://amzn.to/4sOiZyd"
    },
    {
        "id": 7,
        "title": "The Billionaire’s Matchmaker",
        "slug": "the-billionaires-matchmaker",
        "cover": "7-B The Billionaire's Matchmaker.jpg",
        "link": "https://amzn.to/4sjhckW"
    },
    {
        "id": 8,
        "title": "The Billionaire’s Guarded Heart",
        "slug": "the-billionaires-guarded-heart",
        "cover": "08-The Billionaire's Guarded Heart.jpg",
        "link": "https://amzn.to/4sXJ528"
    },
    {
        "id": 9,
        "title": "The Legacy Billionaires Collection (Books 1 and 2)",
        "slug": "legacy-billionaires-box-set-1-2",
        "cover": "BILLIONAIRE BOX SET (1 & 2).jpg",
        "link": "https://www.amazon.com/Legacy-Billionaires-Collection-Books-Novellas-ebook/dp/B0GD11HHQ5",
        "is_collection": True
    },
    {
        "id": 10,
        "title": "The Legacy Billionaires Collection (Books 3 and 4)",
        "slug": "legacy-billionaires-box-set-3-4",
        "cover": "BILLIONAIRES BOX SET 3 & 4.jpg",
        "link": "https://amzn.to/4dtzPhp",
        "is_collection": True
    }
]

generated_anchors = []

for b in books:
    # Get HTML blurb
    blurb_content = blurbs_dict.get(b['title'], "Warm, small-town romance.")
    
    # Simple formatting: double line breaks become paragraphs
    paragraphs = blurb_content.split('  ')
    if len(paragraphs) == 1:
        paragraphs = blurb_content.split('\n\n')
    
    blurb_html = "".join([f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()])
    
    # Safe short blurb
    safe_short_blurb = paragraphs[0].replace('"', '&quot;')[:150] + "..." if paragraphs else ""
    
    buy_html = f'<a href="{b["link"]}" target="_blank" class="btn btn-primary" rel="noopener">Buy on Amazon</a>'
    
    series_tag = f"The Legacy Billionaires #{b['id']}" if not b.get('is_collection') else "The Legacy Billionaires Collection"
    
    filename = f"{b['slug']}-book-page.html"
    
    html = TEMPLATE.format(
        title=b['title'].replace("’", "'"),
        filename=filename,
        short_blurb=safe_short_blurb.replace("’", "'"),
        cover_image=b['cover'],
        series_tag=series_tag,
        blurb_html=blurb_html,
        buy_button_html=buy_html
    )
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Generated {filename}")
    
    # Store anchor for series page updates
    safe_card_title = b["title"].replace("’", "'")
    anchor = f'<a href="./{filename}" class="book-card-link"><div class="book-card"><figure class="book-cover"><img src="media/files/{b["cover"]}" alt="{b["title"]} Cover" loading="lazy" data-is-external-image="true"></figure><p class="book-title">{safe_card_title}</p><p class="book-series-tag">{series_tag}</p></div></a>'
    generated_anchors.append(anchor)

# Now, we update the legacy-billionaires-series-page.html grid
with open("legacy-billionaires-series-page.html", "r", encoding="utf-8") as f:
    series_html = f.read()

grid_html = '\n'.join(generated_anchors)
series_html = re.sub(
    r'<div class="series-featured-grid--large">.*?</div></div></section>', 
    f'<div class="series-featured-grid--large">\n{grid_html}\n</div></div></section>', 
    series_html, 
    flags=re.DOTALL
)

with open("legacy-billionaires-series-page.html", "w", encoding="utf-8") as f:
    f.write(series_html)

print("legacy-billionaires-series-page.html updated successfully!")
