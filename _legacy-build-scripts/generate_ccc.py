import re

with open("the-great-christmas-disaster-book-page.html", "r", encoding="utf-8") as f:
    template = f.read()

b = {
    "title": "The Case of the Stolen Time Capsule",
    "slug": "the-case-of-the-stolen-time-capsule",
    "cover": "1-CCC.png",
    "link": "https://amzn.to/4hb5Srn", # Example link or empty
    "blurb": "<p>A cozy mystery set in a small town where everyone is a suspect but no one is truly malicious. Follow along as the Closed Case Club solves the mystery of the stolen time capsule before the town's centennial celebration is ruined.</p>"
}

series_tag = "The Closed Case Club #1"
filename = f"{b['slug']}-book-page.html"

html = template
html = html.replace("The Great Christmas Disaster Book Page", b["title"] + " Book Page")
html = html.replace("Love Only #1", series_tag)
html = html.replace("1-LO The Great Christmas Disaster.jpg", b["cover"])
html = html.replace("The Great Christmas Disaster", b["title"])
html = html.replace("the-great-christmas-disaster-book-page.html", filename)

# Replace Button
btn_replacement = '<button class="btn btn-primary" style="cursor:not-allowed; opacity:0.7;" disabled>COMING SOON</button>'
html = html.replace('<a href="https://amzn.to/476J978" target="_blank" class="btn btn-primary" rel="noopener">Buy on Amazon </a>', btn_replacement)

# Replace blurb
html = re.sub(r"<div id=\"blurb\" class=\"book-blurb\">.*?</div></div></section>", 
              "<div id=\"blurb\" class=\"book-blurb\">\n<h2>" + b["title"] + "</h2>\n" + b["blurb"] + "\n</div></div></section>", html, flags=re.DOTALL)
              
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
    
print(f"Generated {filename}")
