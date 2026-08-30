from sys import path
from pathlib import Path

path.append(str(Path(__file__).resolve().parent.parent))

from file_selector import select_image
from emotion_analyzer import analyze_emotion
from result_manager import create_result, save_result

image_path = select_image()

if not image_path:
    print("No image selected.")
    exit()

emotion_result = analyze_emotion(image_path)

result = create_result(emotion_result)

save_result(result)

print("Result saved successfully.")
print(result)