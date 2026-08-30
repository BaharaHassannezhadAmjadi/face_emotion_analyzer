from deepface import DeepFace

def detect_faces(image_path):
    try:
        results = DeepFace.extract_faces(img_path=image_path,
                                         detector_backend="retinaface", 
                                         enforce_detection=True,
                                         align=True
                                        )

        return results

    except Exception as error:
        raise RuntimeError(f"Face detection failed: {error}") from error