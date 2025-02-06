from dataclasses import dataclass

@dataclass
class GameInfo:
    ''' Data Class for storing game specific information '''
    link: str
    title: str
    language: str = 'english'

    def _display_info(self) -> None:
        ''' Prints the game title and link '''

        return(
            f"Title: {self.title}",
            f"Link: {self.link}",
            f"Language: {self.language}",
        )

    def __str__(self) -> str:
        return f"{self.title} in {self.language}"


    def to_dict(self) -> dict:
        ''' Returns the game info as a dictionary '''

        return {
            "title": self.title,
            "link": self.link,
            "language": self.language
        }
