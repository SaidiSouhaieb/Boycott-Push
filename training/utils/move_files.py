import os
import shutil
import random


def dir_not_exist_create(dir_path):
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        os.makedirs(dir_path)


def move_files(files, src_dir, data_version, dir_type):
    training_data_path = f"training/data/v{data_version}/"
    dir_not_exist_create(training_data_path)

    destination_dir = os.path.join(
        training_data_path,
        dir_type,
        "train",
    )
    dir_not_exist_create(destination_dir)

    for file in files:
        file_path = os.path.join(src_dir, file)
        file_destination = os.path.join(destination_dir, file)
        shutil.copyfile(file_path, file_destination)

    return destination_dir


def move_random_files(src_dir, dest_dir, num_files=2):
    """
    Move a specified number of random files from src_dir to dest_dir.
    """
    files = os.listdir(src_dir)
    if len(files) < num_files:
        num_files = len(files)  # In case there are fewer files than requested
    random_files = random.sample(files, num_files)

    for file in random_files:
        shutil.copy(os.path.join(src_dir, file), os.path.join(dest_dir, file))
        print(f"Moved {file} from {src_dir} to {dest_dir}")
