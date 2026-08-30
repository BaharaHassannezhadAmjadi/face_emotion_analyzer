from deepface import DeepFace

def analyze_emotion(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path,
                                  actions=["emotion"],
                                  detector_backend="retinaface",
                                  enforce_detection=True
                                )

        return result

    except Exception as error:
        raise RuntimeError(f"Emotion analysis failed: {error}") from error