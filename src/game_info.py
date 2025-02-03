from dataclasses import dataclass

@dataclass
class GameInfo:
    ''' Data Class for storing game specific information '''
    link: str
    title: str

    def display_info(self) -> None:
        ''' Prints the game title and link '''

        print(
            f"Title: {self.title}",
            f"Link: {self.link}",
            "Language: English", # should be made variable
            sep="\n"
        )

        return None
