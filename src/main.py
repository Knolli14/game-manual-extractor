from src.extractor import Extractor

def download_all_manuals(pages: int=1) -> None:
    ''' Entry point for dwonloading all pdfs'''

    extractor = Extractor().get_all_game_infos(last_page_number=pages)

    # game: GameInfo
    for game in extractor.games_list:
        extractor.download_manual(game)

    print("\n", "-" * 10, "Finished downloading all manuals", "-" * 10,)

    return None

if __name__ == "__main__":
    download_all_manuals()
