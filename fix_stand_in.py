import os
import shutil
import glob

# 1. Image rename
old_name = "media/files/1-B The Billionaire's Stand-In Fiancée.jpg"
new_name = "media/files/1-b-stand-in-fiancee.jpg"
if os.path.exists(old_name):
    os.rename(old_name, new_name)

# 2. HTML and script updates
for file in glob.glob("*.html") + ["build_legacy_pages.py"]:
    with open(file, "r") as f:
        content = f.read()
    # Replace both variations of the e acute
    content = content.replace("1-B The Billionaire's Stand-In Fiancée.jpg", "1-b-stand-in-fiancee.jpg")
    content = content.replace("1-B The Billionaire's Stand-In Fiancée.jpg", "1-b-stand-in-fiancee.jpg")
    with open(file, "w") as f:
        f.write(content)

# 3. Banner swap
penthouse_banner = "media/files/banners/legacy_billionaires_banner_new.png"
live_banner = "media/files/banners/legacy-billionaires-banner-new.png"
if os.path.exists(penthouse_banner):
    shutil.copy(penthouse_banner, live_banner)

print("Fixes applied.")
