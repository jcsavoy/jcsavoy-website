from PIL import Image
import os

input_path = "/Users/jeanmason/.gemini/antigravity/brain/07e43dbd-6649-4fb9-b693-d973ab8fe80f/facebook_banner_jc_savoy_1773982161561.png"
output_dir = "/Users/jeanmason/Library/Mobile Documents/com~apple~CloudDocs/AAA DOCUMENTS/JC SAVOY/AntiGravity/JC Savoy Website/jcsavoy-website-repo/media/files/banners"

img = Image.open(input_path)
print(f"Original size: {img.width}x{img.height}")

# Resize so width is exactly 1200
new_width = 1200
new_height = int((new_width / img.width) * img.height)
img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
print(f"Scaled size: {img_resized.width}x{img_resized.height}")

# Target dimensions
target_h = 500

# Top Crop
# Since the text is around the middle and the cat is at the bottom, 
# a center crop might be best, but we'll generate three versions.

# Center Crop
upper_center = (new_height - target_h) // 2
crop_center = img_resized.crop((0, upper_center, 1200, upper_center + target_h))
crop_center.save(os.path.join(output_dir, "facebook_banner_jc_savoy_1200x500_center.png"))

# Offset Crop (Weighted slightly towards the bottom to keep the cat if it's low)
upper_offset = int((new_height - target_h) * 0.70)
crop_offset = img_resized.crop((0, upper_offset, 1200, upper_offset + target_h))
crop_offset.save(os.path.join(output_dir, "facebook_banner_jc_savoy_1200x500.png"))

print("Cropped banners generated!")
