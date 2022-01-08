from typing import List
from datetime import datetime
from user import User

class Channel:

    def __init__(self, server: str, id: str, name: str, description: str = "", avatar: str = "") -> None:
        self.server = server
        self.id = id
        self.name = name
        self.description = description
        self.avatar = avatar
        self.users:List[User] = []

    def get_user(self, id) -> User:
        for user in self.users:
            if user.id == id:
                return user
        return None

    @property
    def usernames(self) -> List[datetime]:
        return [user.name for user in self.users]

    @property
    def timestamps(self) -> List[datetime]:
        return sum([user.timestamps for user in self.users], [])
    
    @property
    def words(self) -> List[str]:
        return sum([user.words for user in self.users], [])
    
    @property
    def emojis(self) -> List[str]:
        return sum([user.emojis for user in self.users], [])

    @property
    def reactions(self):
        return sum([user.reactions for user in self.users], [])

    @property
    def mentions(self) -> List[str]:
        return sum([user.mentions for user in self.users], [])

    @property
    def user_message_count(self) -> List:
        return [user.message_count for user in self.users]
    
    def user_message_counter(self) -> List[tuple]:
        return sorted(list(zip(self.usernames, self.user_message_count)), 
                      key=lambda x: x[1], reverse=True)
