import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the banner title overlay block
# Example: <div class="banner-title-overlay"><h3>Love Only</h3></div>
pattern = r'<div class="banner-title-overlay">\s*<h3.*?>.*?</h3>\s*</div>'
html = re.sub(pattern, "", html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Title overlays removed.")
