from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_IMAGE = OUTPUT_DIR / "analyzed_image.jpg"

RESULT_FILE = BASE_DIR / "results.json"

DETECTOR_BACKEND = "retinaface"

ENFORCE_DETECTION = True

ALIGN_FACES = True
