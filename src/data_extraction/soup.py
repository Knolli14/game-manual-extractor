import requests

from bs4 import BeautifulSoup, Tag, ResultSet
from src.config import SEARCH_URL
from typing import Dict, Callable, Optional




def get_soup(params: Optional[Dict] = None) -> BeautifulSoup:
    ''' Returns a BeautifulSoup object from the search page '''

    params = params if params else {}
    response = requests.get(SEARCH_URL, params=params)
    soup = BeautifulSoup(response.content, "html.parser")

    return soup


def get_last_page_number(soup: BeautifulSoup) -> int:
    ''' Extracts the last page number from the pages bar at the bottom of the search page '''

    get_page_number_from_tag: Callable[[Tag], int] =\
        lambda tag: int(tag.get('href').split('=')[-1])

    page_tags = get_page_bar_tags(soup)
    last_tag = max(page_tags, key=get_page_number_from_tag)
    last_page_number = get_page_number_from_tag(last_tag)

    return last_page_number


def get_page_bar_tags(soup: BeautifulSoup) -> ResultSet:
    ''' Extracts the page bar tags from the search page '''

    return soup.find_all(
        'a',
        class_ = 'page-link'
    )


def get_game_tags(soup: BeautifulSoup) -> ResultSet:
    ''' Extracts the tags containing the game information from the search page '''

    return soup.find_all(
        class_="btn btn-sm btn-secondary mb-1",
        title="In "+"English"
    )
