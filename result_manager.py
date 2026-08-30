import json
from datetime import datetime


def create_result(emotion_result):
    faces = []

    for index, emotion_data in enumerate(emotion_result, start=1):
        face_result = {
            "face_id": index,
            "dominant_emotion": emotion_data["dominant_emotion"],
            "emotion_scores": {
                emotion: float(score)
                for emotion, score in emotion_data["emotion"].items()
            },
            "face_confidence": float(emotion_data["face_confidence"]),
            "face_region": emotion_data["region"]
        }

        faces.append(face_result)

    result = {
        "timestamp": datetime.now().isoformat(),
        "face_count": len(faces),
        "faces": faces
    }    

    return result

def save_result(result, file_path="results.json"):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)