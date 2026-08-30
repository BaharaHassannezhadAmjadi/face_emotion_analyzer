import cv2
from pathlib import Path

def draw_results(image_path, results, output_path=None):
    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    for face in results:
        region = face["face_region"]

        x = int(region["x"])
        y = int(region["y"])
        w = int(region["w"])
        h = int(region["h"])

        emotion = face["dominant_emotion"]

        scores = face["emotion_scores"]

        confidence = scores[emotion] 

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

        label = f"{emotion.capitalize()} - {confidence:.2f}%"

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        font_thickness = 2
        padding = 5

        text_size = cv2.getTextSize(
            label,
            font,
            font_scale,
            font_thickness
        )

        text_width = text_size[0][0]
        text_height = text_size[0][1]

        box_x1 = x
        box_y1 = max(y - text_height - 2 * padding, 0)
        box_x2 = x + text_width + 2 * padding
        box_y2 = max(y, text_height + 2 * padding)

        cv2.rectangle(
            image,
            (box_x1, box_y1),
            (box_x2, box_y2),
            (255, 255, 255),
            -1
        )

        cv2.putText(
            image,
            label,
            (x + padding, box_y2 - padding),
            font,
            font_scale,
            (0, 0, 0),
            font_thickness,
            cv2.LINE_AA
        )

    if output_path:
        output_path = Path(output_path) 

        output_path.parent.mkdir(parents=True, exist_ok=True)

        success = cv2.imwrite(str(output_path), image)

        if not success:
            raise IOError(f"Could not save image: {output_path}")

    return image

def show_image(image, window_name="Face Emotion Analyzer"):
    cv2.imshow(window_name, image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()   