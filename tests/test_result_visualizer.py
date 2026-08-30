from sys import path
from pathlib import Path

path.append(str(Path(__file__).resolve().parent.parent))


from file_selector import select_image
from emotion_analyzer import analyze_emotion
from result_manager import create_result
from result_visualizer import draw_results, show_image

image_path = select_image()

if not image_path:
    print("No image selected.")
    exit()

emotion_result = analyze_emotion(image_path)

result = create_result(emotion_result)

output_image = draw_results(
    image_path,
    result["faces"],
    "output/analyzed_image.jpg"
)

show_image(output_image)