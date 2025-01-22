import os
from .move_files import move_files


def get_brand_dirs(data_dir):
    """
    Retrieve all valid brand directories, excluding hidden files and zips.
    """
    return [
        brand
        for brand in os.listdir(data_dir)
        if brand != ".DS_Store" and not brand.endswith(".zip")
    ]


def process_brand(brand, data_dir, data_version):
    """
    Move images and labels for a given brand, returning paths to training data.
    """
    brand_dir = os.path.join(data_dir, brand, "train")

    images_dir = os.path.join(brand_dir, "images")
    labels_dir = os.path.join(brand_dir, "labels")

    brand_images = os.listdir(images_dir)
    brand_labels = os.listdir(labels_dir)

    images_training_data_path = move_files(
        brand_images, images_dir, data_version, dir_type="images"
    )
    labels_training_data_path = move_files(
        brand_labels, labels_dir, data_version, dir_type="labels"
    )

    print(f"Finished moving files for {brand}")
    return images_training_data_path, labels_training_data_path
