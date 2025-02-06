import json
import requests

from pathlib import Path
from typing import Dict, List
from dataclasses import asdict

from src.config import DATA_DIR, PDF_DIR

def _get_file_path(directory: Path, file_name: str, extension: str) -> Path:
    """ Returns the path to the file """

    return directory / f"{file_name}.{extension}"


def load_json(file_name: str) -> Dict:
    """ Loads the games list from a json file """

    file_path = _get_file_path(DATA_DIR, file_name, "json")

    if file_path.exists():
        print(f"Loading Games List from {file_path}")

        with open(file_path) as file:
            json_data = json.load(file)
            return json_data

    else:
        print("No such file!")
        return None


def save_as_json(file_name: str, games_list: List[Dict]) -> None:
    """ Saves the games list to a json file """

    file_path = _get_file_path(DATA_DIR, file_name, "json")
    print(f"Saving Games List to {file_path}")

    with open(file_path, 'w') as file:
        json.dump(games_list, file, default=asdict, indent=4)

    return None


def download_pdf(link: str, title: str, **kwargs) -> None:
    """ Downloads the pdf from the url """

    file_path = _get_file_path(PDF_DIR, title, "pdf")
    response = requests.get(link)

    if response.status_code == 200:
        print(f"\nDownloading {title}")

        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"-> Successfully downloaded to {file_path}")

    else:
        print(f"Failed to download {title}")

    return None
