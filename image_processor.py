import cv2

def load_image(file_path):
    image = cv2.imread(file_path)

    if image is None:
        raise ValueError("The selected image could not be loaded.")

    return image