from PIL import Image, ImageDraw, ImageFont
from .item_labels import ITEM_LABELS


def detect_brand(model, image_path, show=False):
    """
    Find the data in the image using the YOLO model
    """
    model_results = model(image_path)
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    label = ""

    font_size = 50
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    detected_objects = []
    captcha_result = ""
    boxes_data = []

    for result in model_results:
        for box in result.boxes:
            box_data = {"xyxy": box.xyxy[0].tolist(), "label": str(box.cls.item())}
            boxes_data.append(box_data)

    for box in boxes_data:
        label = ITEM_LABELS[box["label"]]
        box_coords = box["xyxy"]
        detected_objects.append((box_coords))

        for i in range(3):
            draw.rectangle(
                [
                    box_coords[0] - i,
                    box_coords[1] - i,
                    box_coords[2] + i,
                    box_coords[3] + i,
                ],
                outline="red",
            )
        draw.text((box_coords[0], box_coords[1] - 20), label, fill="red", font=font)

    if show:
        img.show()
    return label.lower()
