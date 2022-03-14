import logging

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Loggers
logger = logging.getLogger(__name__)

# Directory Paths
BASE_DIR = Path.cwd()
RESULTS_DIR = BASE_DIR / "api" / "assets" / "results"
RESULTS_WAV_DIR = BASE_DIR / "api" / "assets" / "results_wav"
RESOURCES_DIR= BASE_DIR /  "api" / "resources"
STATIC_DIR = BASE_DIR / "api" / "static"

FISH_CSV_DIR = RESOURCES_DIR / "fish_data.csv"
MODEL_PATH = RESOURCES_DIR / "model.pickle"
# Formattings
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DB_RESULT_DATE_TIME_FORMAT = '%Y-%m-%dT%H: %M: %S'

