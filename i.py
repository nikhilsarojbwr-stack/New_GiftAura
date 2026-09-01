import os
import glob
from PIL import Image

# Configuration
INPUT_DIR = "static/images/celebrations"   # folder containing original images
OUTPUT_DIR = INPUT_DIR                     # overwrite with webp (you can backup first)
QUALITY = 85                               # WebP quality (0-100)
TARGET_SIZES = {
    # pattern: (max_width, max_height)
    "hero-event-scene": (1200, 800),       # hero image – displayed ~746x420 -> 2x = 1492x840
    "timeline-": (400, 400),               # timeline images displayed 137x137 -> 2x = 274x274
    "cta-event-family": (1200, 800),       # cta image
    "vidhi": (600, 900),                   # founder photo – displayed 634x953
    "nikhil": (600, 900),
    "branch-left": (300, 600),             # decorative branch, small
    # add more patterns as needed
}
DEFAULT_MAX_SIZE = (800, 800)              # fallback for other images

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
        # Preserve alpha for PNGs, otherwise convert to RGB
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
        else:
            img = img.convert("RGB")

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
        original_size = os.path.getsize(input_path) / 1024
        new_size = os.path.getsize(output_path) / 1024
        print(f"✅ {os.path.basename(input_path)}: {original_size:.1f}KB → {new_size:.1f}KB ({new_width}x{new_height})")
    except Exception as e:
        print(f"❌ Error processing {input_path}: {e}")

def main():
    # Find all image files recursively (including subfolders)
    extensions = ("*.jpg", "*.jpeg", "*.png")
    image_files = []
    for ext in extensions:
        # Use **/* to search subdirectories
        pattern = os.path.join(INPUT_DIR, "**", ext)
        image_files.extend(glob.glob(pattern, recursive=True))

    if not image_files:
        print(f"No images found in {INPUT_DIR}")
        return

    print(f"Found {len(image_files)} image(s). Processing...")

    for file_path in image_files:
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)

        # Build WebP output path (preserve folder structure if any)
        rel_path = os.path.relpath(file_path, INPUT_DIR)
        rel_dir = os.path.dirname(rel_path)
        output_dir = os.path.join(OUTPUT_DIR, rel_dir) if rel_dir != '.' else OUTPUT_DIR
        os.makedirs(output_dir, exist_ok=True)

        webp_path = os.path.join(output_dir, f"{name}.webp")

        # Skip if WebP already exists (optional: add --force flag)
        if os.path.exists(webp_path):
            print(f"⏭️  {os.path.basename(file_path)} → {os.path.basename(webp_path)} already exists, skipping.")
            continue

        target_size = get_target_size(filename)
        resize_and_convert(file_path, webp_path, target_size)

    print("✅ All images processed.")

if __name__ == "__main__":
    main()