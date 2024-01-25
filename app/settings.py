import pathlib

from config import get_config

BASE_DIR = pathlib.Path(__file__).parent
CONFIG_PATH = BASE_DIR / "config" / "config.yaml"

config = get_config(CONFIG_PATH)
