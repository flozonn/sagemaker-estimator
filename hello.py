import argparse
import json
import os


hyperparams_path = "/opt/ml/input/config/hyperparameters.json"
if os.path.exists(hyperparams_path):
    with open(hyperparams_path, "r") as f:
        hyperparameters = json.load(f)

name = hyperparameters.get("name", None)
print("Hello! "+ name)