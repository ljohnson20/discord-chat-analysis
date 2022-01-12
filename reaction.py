import itertools

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
            "name": "hello",
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

class Emoji:

    new_id = itertools.count()

    def __init__(self, id, name, url) -> None:
        self.id = id if id else next(Emoji.new_id)
        self.name = name
        self.url = url

    # Download image for use
    # Maybe strip background and scale?
    def get_image(self):
        self.url
        pass
