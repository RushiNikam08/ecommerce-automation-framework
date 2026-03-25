import yaml
import os

def load_config(env="dev"):
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", f"{env}.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)