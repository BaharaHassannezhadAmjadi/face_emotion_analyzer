from sys import path
from pathlib import Path

path.append(str(Path(__file__).resolve().parent.parent))

from file_selector import select_image

image_path = select_image()

if image_path:
    print("Selected image:", image_path)

else:
    print("No image selected.")    