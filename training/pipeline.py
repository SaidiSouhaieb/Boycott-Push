import sys
import argparse

from utils.merge_data import merge_data
from utils.finetuning import train

if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(description="Training script")
        parser.add_argument("data_version", type=int, help="Version of the dataset")
        parser.add_argument(
            "number_epochs", type=int, help="Number of epochs for training"
        )
        args = parser.parse_args()
        data_version = args.data_version
        number_epochs = args.number_epochs

        data_dir = "data/annotated/"
        merge_data(data_dir, data_version)

        train(data_version=data_version, number_epochs=number_epochs)

    except argparse.ArgumentTypeError as e:
        print(f"Argument parsing error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error in the script: {e}")
        sys.exit(1)
