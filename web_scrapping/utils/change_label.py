import os
import argparse


def update_first_number_in_file(file_path, label):
    with open(file_path, "r") as file:
        content = file.read()

    numbers = content.split()

    try:
        numbers[0] = str(label)
    except IndexError:
        print(f"File {file_path} does not contain any numbers.")

    updated_content = " ".join(numbers)

    with open(file_path, "w") as file:
        file.write(updated_content)


def update_files_in_folder(brand, label):
    folder_path = f"data/annotated/{brand}/train/labels"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            print(f"Updating file: {file_path}")
            update_first_number_in_file(file_path, label)
