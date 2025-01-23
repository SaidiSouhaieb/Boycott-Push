import argparse
from ultralytics import YOLO
import sys
import ruamel.yaml
import os


def change_config_version(version, yaml_path):
    old_version = version - 1
    yaml = ruamel.yaml.YAML()

    try:
        if not os.path.exists(yaml_path):
            raise FileNotFoundError("config.yaml file not found!")

        with open(yaml_path) as fp:
            data = yaml.load(fp)

        if "path" not in data:
            raise KeyError("'path' key not found in config.yaml")

        data["path"] = data["path"].replace(f"v{old_version}", f"v{version}")

        with open(yaml_path, "w") as fp:
            yaml.dump(data, fp)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


def train(data_version, number_epochs):
    try:
        model_path = "model/base/yolo11x.pt"
        yaml_path = "training/config.yaml"

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")

        model = YOLO(model_path)
        model.to("cuda")
        model.nc = 16

        change_config_version(data_version, yaml_path)

        print(f"Starting training for {number_epochs} epochs...")
        model.train(data=yaml_path, epochs=number_epochs, batch=6,)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during training: {e}")
        sys.exit(1)
