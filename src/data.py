import json

from pathlib import Path
from typing import Dict, List

#TODO: change to Path Objects

def load_json(file_path: Path) -> Dict:
    """ Loads the games list from a json file """

    if file_path.exists():
        print(f"Loading Games List from {file_path}")

        with open(file_path) as file:
            games_list = json.load(file)
            return games_list

    else:
        print("No such file!")
        return None


def save_json(file_path: Path, games_list: List[Dict]) -> None:
    """ Saves the games list to a json file """
    print(f"Saving Games List to {file_path}")

    with open(file_path, 'w') as file:
        json.dump(games_list, file)
