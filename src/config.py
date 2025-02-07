from pathlib import Path

# First page of empty search
SEARCH_URL = "https://en.1jour-1jeu.com/rules/search?"

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

PDF_DIR = DATA_DIR / "pdf"

MD_DIR = DATA_DIR / "markdown"
