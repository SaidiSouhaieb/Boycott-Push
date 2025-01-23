import os
import sys
import argparse

from utils.move_model import move_model
from utils.evaluation import evaluate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))


def main(add_new_model, show, model_version):
    if add_new_model:
        print("Moving model")
        source_dir = "runs/detect"
        target_base_dir = "model/"
        model_version = move_model(source_dir, target_base_dir)
        print("Model moved")

    print("Starting Evaluation")
    detetctions = evaluate(show, model_version)
    print("Finished Detections")
    print(detetctions)


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Evaluation script")
        parser.add_argument(
            "--new",
            action="store_true",
            help="Move the model before evaluation",
        )

        parser.add_argument(
            "--mv",
            type=str,
            help="Yolo model version",
        )

        parser.add_argument(
            "--show",
            type=lambda x: x.lower() in ["true", "1", "yes"],
            help="Show evaluation results (True/False)",
        )

        args = parser.parse_args()

        main(
            add_new_model=args.new,
            show=(args.show if args.show is not None else True),
            model_version=f"v{args.mv}",
        )

    except argparse.ArgumentTypeError as e:
        print(f"Argument parsing error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error in the script: {e}")
        sys.exit(1)
