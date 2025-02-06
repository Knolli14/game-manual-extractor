from bs4.element import Tag
from src.game_info import GameInfo


def extract_title(url:str) -> str:
    ''' Extract game title out of link without pdf extension'''

    title_full = url.split("/")[-1] \
                    .strip(".pdf")

    return " ".join(title_full.split("-")[1:-1])

def get_donwload_link(tag_result: Tag) -> str:
    return tag_result.get("href")


def get_game_info(tag: Tag) -> GameInfo:
    ''' Extracts link and title info from tag '''

    game_info = GameInfo(
        (link := get_donwload_link(tag)),
        extract_title(link)
    )

    print(f"Extracted {game_info.title}")

    return game_info
