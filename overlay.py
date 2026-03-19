import os
from PIL import Image, ImageDraw, ImageFont

img_path = "media/files/banners/short_story_banner.png"
out_path = "media/files/banners/short_story_banner_labeled.jpg"
text = "Short Story Collections"

img = Image.open(img_path).convert("RGBA")
W, H = img.size

# Find a good font.
font_paths = [
    "/System/Library/Fonts/Supplemental/Baskerville.ttc",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/Library/Fonts/Georgia.ttf",
    "/System/Library/Fonts/Times.ttc"
]
fnt = None
# We want the text to fill roughly 65% of the image width
target_width = W * 0.65
font_size = 10

for path in font_paths:
    if os.path.exists(path):
        fnt = ImageFont.truetype(path, font_size)
        while fnt.getlength(text) < target_width and font_size < 300:
            font_size += 2
            fnt = ImageFont.truetype(path, font_size)
        break

if not fnt:
    fnt = ImageFont.load_default()

txt_layer = Image.new('RGBA', img.size, (255,255,255,0))
d = ImageDraw.Draw(txt_layer)

bbox = d.textbbox((0, 0), text, font=fnt)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x, y = (W - w) / 2, (H - h) / 2

# Shadow logic
shadow_color = (0, 0, 0, 200)
offset = max(2, int(font_size * 0.04))
d.text((x + offset, y + offset), text, font=fnt, fill=shadow_color)
d.text((x - offset//2, y + offset//2), text, font=fnt, fill=shadow_color)

# Draw main text, white
d.text((x, y), text, font=fnt, fill=(255, 255, 255, 255))

out = Image.alpha_composite(img, txt_layer).convert("RGB")
out.save(out_path, quality=95)
print("Saved labeled banner.")
