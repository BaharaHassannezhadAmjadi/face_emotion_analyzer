from sys import path
from pathlib import Path

path.append(str(Path(__file__).resolve().parent.parent))

from file_selector import select_image
from face_detector import detect_faces

image_path = select_image()
faces = detect_faces(image_path)

print(f"Number of faces detected: {len(faces)}")

for index, face in enumerate(faces, start=1):
    print(f"Face {index}:")
    print(face["facial_area"])