import os
from dotenv import load_dotenv
from ultralytics import YOLO
from .detetct_brand import detect_brand
from .item_labels import ITEM_LABELS

load_dotenv()
yolo_model_version = os.environ["YOLO_MODEL_VERSION"]


def evaluate(show, model_version):
    model = YOLO(f"model/{model_version}/best.pt")

    images_dir = "data/validation/images"

    detections = []

    folders_dir = os.listdir(images_dir)
    for folder in folders_dir:
        correct_detections = 0
        images = os.listdir(os.path.join(images_dir, folder))

        for image in images:
            nmb_images = len(images)
            img_path = os.path.join(images_dir, folder, image)
            detected_label = detect_brand(model, img_path, show)

            if detected_label == folder:
                correct_detections += 1

        detetction_result = f"Detected {correct_detections} out of {nmb_images} correct labels for {folder}"
        correct_percentange = (correct_detections / nmb_images) * 100
        detections.append(f"{folder}: {correct_percentange}")

    return detections
