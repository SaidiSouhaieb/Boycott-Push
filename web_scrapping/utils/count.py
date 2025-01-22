import os


def count():
    directory_path = "../datasets"

    dirs = os.listdir(directory_path)

    number_files = 0

    for dir in dirs:
        if dir != ".DS_Store":
            images = os.listdir(os.path.join(directory_path, dir))
            for image in images:
                number_files += 1
    print(f"Number of files: {number_files}")


if __name__ == "__main__":
    count()
