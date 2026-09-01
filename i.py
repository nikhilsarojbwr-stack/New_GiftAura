import os
import glob
from PIL import Image

# Configuration
INPUT_DIR = "static/images"          # folder containing original images
OUTPUT_DIR = INPUT_DIR               # overwrite with webp (you can backup first)
QUALITY = 85                         # WebP quality (0-100)
TARGET_SIZES = {
    # pattern: (max_width, max_height)  # None means preserve original
    "hero-event-scene": (1200, 800),     # hero image – displayed ~746x420 -> 2x = 1492x840
    "timeline-": (400, 400),             # timeline images are displayed 137x137 -> 2x = 274x274, but let's keep some quality
    "cta-event-family": (1200, 800),     # cta image
    "vidhi": (600, 900),                 # founder photo – displayed 634x953, we'll cap width
    "nikhil": (600, 900),
    "branch-left": (300, 600),           # decorative branch, small
    # add more patterns as needed
}
DEFAULT_MAX_SIZE = (800, 800)        # fallback for other images

def get_target_size(filename):
    """Return (max_width, max_height) based on filename pattern."""
    for pattern, size in TARGET_SIZES.items():
        if pattern in filename:
            return size
    return DEFAULT_MAX_SIZE

def resize_and_convert(input_path, output_path, max_size):
    """Open image, resize (if larger than max), convert to WebP and save."""
    try:
        img = Image.open(input_path)
        # Convert RGBA to RGB if needed (WebP supports alpha, but JPEG doesn't)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")  # Keep alpha for PNGs
        else:
            img = img.convert("RGB")

        # Calculate new dimensions preserving aspect ratio
        original_width, original_height = img.size
        max_width, max_height = max_size

        # If image is already smaller than target, keep original size
        if original_width <= max_width and original_height <= max_height:
            new_width, new_height = original_width, original_height
        else:
            ratio = min(max_width / original_width, max_height / original_height)
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)

        if (new_width, new_height) != (original_width, original_height):
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Save as WebP
        img.save(output_path, "webp", quality=QUALITY, optimize=True)
        print(f"✅ Saved {output_path} ({new_width}x{new_height})")
    except Exception as e:
        print(f"❌ Error processing {input_path}: {e}")

def main():
    # Find all image files
    extensions = ("*.webp", "*.jpeg", "*.png")
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(INPUT_DIR, ext), recursive=True))

    if not image_files:
        print("No images found in", INPUT_DIR)
        return

    # Process each file
    for file_path in image_files:
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        webp_path = os.path.join(OUTPUT_DIR, f"{name}webp")

        # Skip if WebP already exists (you can force regenerate by deleting)
        if os.path.exists(webp_path):
            print(f"⏭️  WebP already exists: {webp_path}, skipping...")
            continue

        target_size = get_target_size(filename)
        resize_and_convert(file_path, webp_path, target_size)

        # Optional: rename original to .backup or delete? We'll keep them for safety.
        # To avoid serving originals, rename them (e.g., add .old) or move to backup.
        # We'll keep them, but later in HTML we'll reference webp.

    print("✅ All images processed.")

if __name__ == "__main__":
    main()