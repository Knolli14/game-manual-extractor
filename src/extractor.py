from src.data import load_json, save_as_json, download_pdf
from src.soup import get_soup, get_last_page_number, get_game_tags
from src.utils import get_game_info
from src.game_info import GameInfo

from typing import Optional, Dict, List

class Extractor:
    ''' Class for downloading and extracting game information from 1jour-1jeu.com '''

    #TODO: make dic as arg possible
    def __init__(self, games_list: List[GameInfo]=None):
        self.games_list = games_list if games_list else []


    def get_all_game_infos(self, last_page_number: Optional[int]=None) -> 'Extractor':
        ''' Extracts the list with links and title of all available games '''

        soup = get_soup()
        last_page_number = last_page_number \
            if last_page_number \
            else get_last_page_number(soup)

        for page in range(1,last_page_number+1):
            print(f"-> Extracting games from page {page}")
            soup = get_soup({"page": page})

            # extract game infos from soup and add them to games_list
            self.games_list.extend([get_game_info(tag)
                                    for tag in get_game_tags(soup)])

            print(f"-> Finished extracting games from page {page}", 30*"-", sep="\n")

        print(f"Successfully extracted {len(self.games_list)} games")

        return self


    def save_games_list(self, file_name: str='games_list') -> None:
        ''' Saves the games list to a json file '''

        save_as_json(file_name, self.games_list)
        print(f"Successfully saved Games List")

        return None


    def download_manual(self, game: GameInfo|str) -> None:
        ''' Downloads the manual for a specific game '''

        if isinstance(game, str):
            # find correct gameinfo in games_list
            pass

        download_pdf(**game.to_dict())

        return None


    # Methods for handling games list

    def search_games_list(self, title: str) -> List[Dict]:
        ''' Searches the games list for a specific title '''

        return [game for game in self.games_list if title in game['title']]



    # Class Methods

    @classmethod
    def from_json(cls, file_path: str) -> Optional['Extractor']:

        games_list = load_json(file_path)
        if games_list:
            print(f"Successfully loaded Games List into Extractor")
            return cls(games_list=games_list)

        else:
            print("No such file!")
            return None
