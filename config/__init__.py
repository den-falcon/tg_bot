import yaml


def get_config(path):
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
        return parsed_config
