import os

from .test_image_numbers import test_image_numbers
from .move_files import move_random_files, dir_not_exist_create
from .process_brands import process_brand, get_brand_dirs


def merge_data(data_dir, data_version):
    """
    Main process to handle moving images and labels for all brands.
    """
    brands_dirs = get_brand_dirs(data_dir)

    for brand in brands_dirs:
        images_training_data_path, labels_training_data_path = process_brand(
            brand, data_dir, data_version
        )

        # Create validation directories if they do not exist
        valid_images_dir = images_training_data_path.replace("/train", "/valid")
        valid_labels_dir = labels_training_data_path.replace("/train", "/valid")

        print(valid_images_dir, "valid\n\n\n\n\n")
        print(valid_labels_dir, "valid\n\n\n\n\n")

        dir_not_exist_create(valid_images_dir)
        dir_not_exist_create(valid_labels_dir)

        # Move 2 random images and corresponding labels to validation directories
        move_random_files(images_training_data_path, valid_images_dir, num_files=2)
        move_random_files(labels_training_data_path, valid_labels_dir, num_files=2)

        # Test image numbers after processing
        test_image_numbers(images_training_data_path, data_dir)
