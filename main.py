from file_selector import select_image
from face_detector import detect_faces
from emotion_analyzer import analyze_emotion
from result_manager import create_result, save_result
from result_visualizer import draw_results, show_image
from config import OUTPUT_IMAGE, RESULT_FILE

def main():
    print("=== Face Emotion Analyzer ===")

    image_path = select_image()

    if not image_path:
        print("No image selected.")
        return

    print(f"Selected image: {image_path}")

    try:
        faces = detect_faces(image_path)

        if not faces:
            print("No faces detected.")
            return

        print(f"{len(faces)} face(s) detected.")

        emotion_results = analyze_emotion(image_path)

        result = create_result(emotion_results)

        save_result(result, RESULT_FILE)

        output_image = draw_results(
            image_path,
            result["faces"],
            "output/analyzed_image.jpg"
        )

        show_image(output_image)

        print("Analysis completed successfully.")
        print("Result saved to results.json")
        print("Analyzed image saved to output/analyzed_image.jpg")

    except Exception as error:
        print(f"An error occurred: {error}") 

if __name__ == "__main__":
    main()           
