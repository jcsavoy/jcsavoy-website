import os
import shutil
from PIL import Image

src_dir = "/Users/jeanmason/.gemini/antigravity/brain/07e43dbd-6649-4fb9-b693-d973ab8fe80f"
dest_dir = "media/files/banners"

images = {
    "kingsleys_clean": "kingsleys_clean_1773983728338.png",
    "legacy_clean": "legacy_clean_1773983741149.png",
    "whispering_clean": "whispering_clean_1773983754688.png",
    "cozy_clean": "cozy_clean_1773983770108.png"
}

for name, filename in images.items():
    src_path = os.path.join(src_dir, filename)
    dest_path = os.path.join(dest_dir, f"{name}.png")
    
    # Open image
    img = Image.open(src_path)
    w, h = img.size
    print(f"{name}: {w}x{h}")
    
    # If it looks like a collage (some DALL-E panoramic generations put borders or split vertically)
    # Actually, DALL-E generated 1024x1024. The whispering and cozy have distinct horizontal splits.
    if name in ["whispering_clean", "cozy_clean"]:
        # Crop the middle section: the middle third is roughly y=341 to 682
        # Actually I will crop the middle horizontal band.
        img = img.crop((0, h//3, w, 2*h//3))
        print(f"Cropped {name} to {img.size}")
    
    # Save the processed image
    img.save(dest_path)
    print(f"Saved {dest_path}")

