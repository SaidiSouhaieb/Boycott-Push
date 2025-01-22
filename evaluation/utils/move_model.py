import os
import shutil


def move_model(source_dir, target_base_dir):
    new_folders = []
    train_folders = [f for f in os.listdir(source_dir) if f.startswith("train")]
    for folder in train_folders:
        if folder != "train":
            new_folders.append(int(folder.replace("train", "")))

    if not new_folders:
        raise Exception("No 'train(number)' folders found.")

    last_train_folder = os.path.join(
        source_dir, "train" + str(sorted(new_folders)[-1]), "weights"
    )

    if not os.path.exists(last_train_folder):
        raise Exception(f"'weights' folder not found in {last_train_folder}")

    best_model_path = os.path.join(last_train_folder, "best.pt")

    if not os.path.exists(best_model_path):
        raise Exception(f"'best.pt' not found in {last_train_folder}")

    v_folders = [f for f in os.listdir(target_base_dir) if f.startswith("v")]
    if v_folders:
        last_v_folder_num = max([int(f.replace("v", "")) for f in v_folders])
        new_v_folder_num = last_v_folder_num + 1
    else:
        new_v_folder_num = 1

    new_v_folder = os.path.join(target_base_dir, f"v{new_v_folder_num}")

    os.makedirs(new_v_folder, exist_ok=True)

    shutil.move(best_model_path, os.path.join(new_v_folder, "best.pt"))

    print(f"Moved best.pt to {new_v_folder}")
