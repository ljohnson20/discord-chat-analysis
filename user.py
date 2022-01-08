from typing import List
from datetime import datetime

reaction_example = r"""
"reactions": [
    {
        "emoji": {
            "id": null,
            "name": "\uD83D\uDE09",
            "isAnimated": false,
            "imageUrl": "https://twemoji.maxcdn.com/2/svg/1f609.svg"
        },
        "count": 1
    },
    {
        "emoji": {
            "id": "421123828383744021",
            "name": "gay",
            "isAnimated": false,
            "imageUrl": "https://cdn.discordapp.com/emojis/421123828383744021.png"
        },
        "count": 1
    },
    {
        "emoji": {
            "id": "588776075778195459",
            "name": "PepeLaughJumping",
            "isAnimated": true,
            "imageUrl": "https://cdn.discordapp.com/emojis/588776075778195459.gif"
        },
        "count": 1
    }
]
"""

class User:

    def __init__(self, id: str, name: str, nickname: str = "", avatar: str = "") -> None:
        self.id = id
        self.name = name
        if nickname == "":
            self.nickname = name
        else:
            self.nickname = nickname
        self.avatar = avatar
        self.message_count = 0
        self.timestamps:List[datetime] = []
        self.words:List[str] = []
        self.emojis:List[str] = []
        self.reactions = []
        self.mentions:List[str] = []

    @property
    def message_tuple(self):
        return None


