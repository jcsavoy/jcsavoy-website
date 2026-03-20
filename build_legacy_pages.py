import re
import os
import shutil

# First, copy the covers to the media directory if they aren't already there
source_covers_dir = "../The Legacy Billionaires/Covers for The Legacy Billionaires"
dest_media_dir = "media/files"
if os.path.exists(source_covers_dir):
    for filename in os.listdir(source_covers_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            shutil.copy2(os.path.join(source_covers_dir, filename), os.path.join(dest_media_dir, filename))

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

def get_blurb_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Fix regex to not require a space before newline
    parts = re.split(r"(Book \d+:.*?\n|The Legacy Billionaires Collection.*?\n)", text)
    blurbs = {}
    current_title = None
    
    for part in parts:
        part = part.strip()
        if not part: continue
        if part.startswith("Book "):
            current_title = part.split(":")[1].strip()
        elif part.startswith("The Legacy Billionaires Collection"):
            current_title = part.strip()
        elif current_title:
            blurbs[current_title] = part
            
    return blurbs

blurbs_dict = get_blurb_text("legacy_blurbs.txt")

books = [
    {
        "id": 1,
        "title": "The Billionaire’s Stand-In Fiancée",
        "slug": "the-billionaires-stand-in-fiancee",
        "cover": "1-b-stand-in-fiancee.jpg",
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
    
    paragraphs = blurb_content.split('  ')
    if len(paragraphs) == 1:
        paragraphs = blurb_content.split('\n\n')
    
    blurb_html = "".join([f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()])
    
    series_tag = f"The Legacy Billionaires #{b['id']}" if not b.get('is_collection') else "The Legacy Billionaires Collection"
    filename = f"{b['slug']}-book-page.html"
    
    html = template
    html = html.replace("The Great Christmas Disaster Book Page", b["title"].replace("’", "'") + " Book Page")
    html = html.replace("Love Only #1", series_tag)
    html = html.replace("1-LO The Great Christmas Disaster.jpg", b["cover"])
    html = html.replace("The Great Christmas Disaster", b["title"].replace("’", "'"))
    html = html.replace("the-great-christmas-disaster-book-page.html", filename)
    
    # Replace Button
    if b["link"]:
        btn_replacement = f'<a href="{b["link"]}" target="_blank" class="btn btn-primary" rel="noopener">Buy on Amazon</a>'
    else:
        btn_replacement = '<button class="btn btn-primary" style="cursor:not-allowed; opacity:0.7;" disabled>COMING SOON</button>'
        
    html = html.replace('<a href="https://amzn.to/476J978" target="_blank" class="btn btn-primary" rel="noopener">Buy on Amazon </a>', btn_replacement)
    
    # Replace blurb
    html = re.sub(r"<div id=\"blurb\" class=\"book-blurb\">.*?</div></div></section>", 
                  "<div id=\"blurb\" class=\"book-blurb\">\n<h2>" + b["title"].replace("’", "'") + "</h2>\n" + blurb_html + "\n</div></div></section>", html, flags=re.DOTALL)
                  
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Generated {filename}")
    
    # Store anchor for series page updates
    safe_card_title = b["title"].replace("’", "'")
    anchor = f'<a href="./{filename}" class="book-card-link"><div class="book-card"><figure class="book-cover"><img src="media/files/{b["cover"]}" alt="{safe_card_title} Cover" loading="lazy" data-is-external-image="true"></figure><p class="book-title">{safe_card_title}</p><p class="book-series-tag">{series_tag}</p></div></a>'
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
