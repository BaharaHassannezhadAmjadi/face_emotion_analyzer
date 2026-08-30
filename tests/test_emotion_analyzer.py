from sys import path
from pathlib import Path

path.append(str(Path(__file__).resolve().parent.parent))

from file_selector import select_image
from emotion_analyzer import analyze_emotion

image_path = select_image()

if not image_path:
    print("No image selected.")
    exit()
    
results = analyze_emotion(image_path)

print("Emotion analysis completed.")
print(results)