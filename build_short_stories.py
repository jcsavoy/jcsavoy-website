import os
import re

with open("cozy-mysteries-series-page.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Page Title and Meta
html = html.replace("<title>The Closed Case Club - JC Savoy website</title>", "<title>Short Story Collections - JC Savoy website</title>")
html = html.replace("The Closed Case Club Banner", "Short Story Collections Banner")
html = html.replace("Possiible Closed Case Club Banner.jpg", "short_story_banner_labeled.jpg")
html = html.replace("Magnifying glass (rev 1).png", "Book (rev 1).png")
html = html.replace("The Closed Case Club Series", "Short Story Collections Series")
html = html.replace("<h1>The Closed Case Club</h1>", "<h1>Short Story Collections</h1>")
html = html.replace("<p class=\"hero-subtitle\">Small-town sleuthing with heart</p>", "<p class=\"hero-subtitle\">Bite-sized romance and heartwarming tales</p>")
html = html.replace("<p class=\"hero-description\">Small-town sleuthing with heart. Mysteries that keep you guessing without keeping you up at night.</p>", "<p class=\"hero-description\">Quick escapes into the worlds of the Kingsleys and Whispering Falls. Perfect for a cozy afternoon read or a bedtime love story.</p>")

# We don't have a single series shop link for short stories, so we can hide or change the hero button
html = html.replace("<div class=\"hero-cta\"><a href=\"https://amzn.to/4rM8XNt\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Shop the Series on Amazon</a></div>", "")
html = html.replace("<div class=\"hero-cta\"><a href=\"https://www.amazon.com/stores/JC-Savoy/author/B0D2V26K3W\" target=\"_blank\" class=\"btn btn-primary\" rel=\"noopener\">Shop the Series on Amazon</a></div>", "")

html = html.replace("<h2>The Closed Case Club (Cozy Mystery)</h2>", "<h2>Short Story Collections</h2>")

# Replace Grid
new_grid = """
<a href="https://amzn.to/3NzSFJd" target="_blank" class="book-card-link" rel="noopener"><div class="book-card"><figure class="book-cover"><img src="media/files/Featured book 3 cover.jpg" alt="Whispering Falls Short Stories" loading="lazy" data-is-external-image="true"></figure><p class="book-title">Whispering Falls Short Stories</p><p class="book-series-tag">Collection</p></div></a>
<a href="https://amzn.to/3Pz811j" target="_blank" class="book-card-link" rel="noopener"><div class="book-card"><figure class="book-cover"><img src="media/files/Featured book 5 cover.jpg" alt="Kingsleys Sweet Short Stories" loading="lazy" data-is-external-image="true"></figure><p class="book-title">Kingsley's Sweet Short Stories</p><p class="book-series-tag">Collection</p></div></a>
"""

html = re.sub(r"<div class=\"series-featured-grid--large\">.*?</div></div></section>", 
              "<div class=\"series-featured-grid--large\">" + new_grid + "</div></div></section>", html, flags=re.DOTALL)

with open("short-story-collections-series-page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Short story collections page generated!")
