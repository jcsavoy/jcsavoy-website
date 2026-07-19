import re
import os
import shutil

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

books = [
    {
        "id": 1,
        "title": "The Case of the Stolen Time Capsule",
        "slug": "the-case-of-the-stolen-time-capsule",
        "cover": "1-CCC.png",
    },
    {
        "id": 2,
        "title": "The Case of the Disappearing Diner",
        "slug": "the-case-of-the-disappearing-diner",
        "cover": "2-CCC.jpg",
    },
    {
        "id": 3,
        "title": "The Case of the Yuletide Heist",
        "slug": "the-case-of-the-yuletide-heist",
        "cover": "3-CCC.jpg",
    },
    {
        "id": 4,
        "title": "The Case of the Lethal Lemon Drop",
        "slug": "the-case-of-the-lethal-lemon-drop",
        "cover": "4-CCC.jpg",
    },
    {
        "id": 5,
        "title": "The Case of the Deadly Lakeside",
        "slug": "the-case-of-the-deadly-lakeside",
        "cover": "5-CCC.jpg",
    }
]

generated_anchors = []
generic_blurb = "<p>Small-town sleuthing with heart. Mysteries that keep you guessing without keeping you up at night. Follow the Closed Case Club as they unravel secrets, track down suspects, and prove that the most unassuming folks sometimes make the best detectives.</p>"

for b in books:
    series_tag = f"The Closed Case Club #{b['id']}"
    filename = f"{b['slug']}-book-page.html"
    
    html = template
    html = html.replace("The Great Christmas Disaster Book Page", b["title"] + " Book Page")
    html = html.replace("Love Only #1", series_tag)
    
    # Replace the image and title in the correct order to avoid replacing internal parts
    html = html.replace("1-LO The Great Christmas Disaster.jpg", b["cover"])
    html = html.replace("The Great Christmas Disaster", b["title"])
    html = html.replace("the-great-christmas-disaster-book-page.html", filename)
    
    # Replace Button (Amazon links not provided yet)
    btn_replacement = '<a href="https://amzn.to/4rM8XNt" target="_blank" class="btn btn-primary" rel="noopener">Buy on Amazon</a>'
    html = html.replace('<a href="https://amzn.to/476J978" target="_blank" class="btn btn-primary" rel="noopener">Buy on Amazon </a>', btn_replacement)
    
    # Replace blurb
    html = re.sub(r"<div id=\"blurb\" class=\"book-blurb\">.*?</div></div></section>", 
                  f"<div id=\"blurb\" class=\"book-blurb\">\n<h2>{b['title']}</h2>\n{generic_blurb}\n</div></div></section>", html, flags=re.DOTALL)
                  
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Generated {filename}")
    
    # Store anchor for series page updates
    anchor = f'<a href="./{filename}" class="book-card-link"><div class="book-card"><figure class="book-cover"><img src="media/files/{b["cover"]}" alt="{b["title"]} Cover" loading="lazy" data-is-external-image="true"></figure><p class="book-title">{b["title"]}</p><p class="book-series-tag">{series_tag}</p></div></a>'
    generated_anchors.append(anchor)

# Now, we update the cozy-mysteries-series-page.html grid
with open("cozy-mysteries-series-page.html", "r", encoding="utf-8") as f:
    series_html = f.read()

grid_html = '\n'.join(generated_anchors)
series_html = re.sub(
    r'<div class="series-featured-grid--large">.*?</div></div></section>', 
    f'<div class="series-featured-grid--large">\n{grid_html}\n</div></div></section>', 
    series_html, 
    flags=re.DOTALL
)

with open("cozy-mysteries-series-page.html", "w", encoding="utf-8") as f:
    f.write(series_html)

print("cozy-mysteries-series-page.html updated successfully!")
