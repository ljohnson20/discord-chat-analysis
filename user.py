from typing import List
from datetime import datetime
from reaction import Emoji

class User:

    def __init__(self, id: str, name: str, nickname: str = "", avatar: str = "") -> None:
        self.id = id
        self.name = name
        self.nickname = nickname if nickname == "" else name
        self.avatar = avatar
        self.message_count = 0
        self.edit_count = 0
        self.timestamps:List[datetime] = []
        self.words:List[str] = []
        self.emojis:List[str] = []
        self.reactions:List[Emoji] = []
        self.mentions:List[str] = []

    # More info?
    def __str__(self) -> str:
        return f"User '{self.name}' ({self.nickname})"

    # Could be fleshed out further?
    def __repr__(self) -> str:
        return (f"User(id={self.id}, name={self.name}, nickname={self.nickname}, "
                f"messages={self.message_count}), words={len(self.words)}")

    @property
    def message_tuple(self):
        return None


