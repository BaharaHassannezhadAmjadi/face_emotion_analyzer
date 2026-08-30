from sys import path
from pathlib import Path

path.append(str(Path(__file__).resolve().parent.parent))

from file_selector import select_image
from image_processor import load_image

image_path = select_image()

if not image_path:
    print("No image selected.")
    exit()
    
image = load_image(image_path)

print("Image loaded successfully.")
print("Image shape:", image.shape)