import sys
import argparse

from utils.change_label import update_files_in_folder
from utils.count import count
from utils.move_dataset import organize_folders
from utils.scrap import scrap

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Update the first number in label files."
        )
        parser.add_argument(
            "brand", type=str, help="The brand name to update files for."
        )
        parser.add_argument("label", type=int, help="The number to replace 0 with.")

        args = parser.parse_args()

        scrap()
        update_files_in_folder(args.brand, args.label)
        count()

        source_directory = "web_scrapping/scrapping/datasets"
        destination_directory = "data/raw"
        organize_folders(source_directory, destination_directory)
    except argparse.ArgumentTypeError as e:
        print(f"Argument parsing error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error in the script: {e}")
        sys.exit(1)
