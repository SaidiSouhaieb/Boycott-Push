import os


def count_files(directory_path):
    files = os.listdir(directory_path)

    number_files = 0

    for file in files:
        if file.endswith(".jpg"):
            number_files += 1
    print(f"Number of files: {number_files}")


def count_annotated_images(dir_path):
    dirs = os.listdir(dir_path)

    number_files = 0

    for dir in dirs:
        if dir != ".DS_Store" and not dir.endswith("zip"):
            train_images_path = os.path.join(dir_path, dir, "train", "images")
            images = os.listdir(train_images_path)
            for image in images:
                number_files += 1
    print(f"Number of files: {number_files}")


def test_image_numbers(training_data_path, annotated_dir_path):
    if count_files(training_data_path) == count_annotated_images(annotated_dir_path):
        print("Success: The images have correctly been copied!")
    else:
        print("Error: The images haven't been correctly copied!")
