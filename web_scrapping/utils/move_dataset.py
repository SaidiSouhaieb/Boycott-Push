import os
import shutil


def organize_folders(source_dir, destination_dir):
    try:
        folders = [
            f
            for f in os.listdir(source_dir)
            if os.path.isdir(os.path.join(source_dir, f))
        ]

        for folder in folders:
            if dir != ".DS_Store":
                first_word = folder.split("-")[0].strip()

                new_folder_path = os.path.join(destination_dir, first_word)
                os.makedirs(new_folder_path, exist_ok=True)

                shutil.move(
                    os.path.join(source_dir, folder),
                    os.path.join(new_folder_path, folder),
                )
                print(f'Moved folder "{folder}" to "{new_folder_path}"')

    except Exception as e:
        print(f"An error occurred: {e}")
