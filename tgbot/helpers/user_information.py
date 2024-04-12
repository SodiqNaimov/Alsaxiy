from tgbot.helpers.database import SQLite
from tgbot.files.config import db_path

from telebot.types import Message


class User_info:
    def __init__(self, message: Message):
        self.db = SQLite(db_path)

        self.chat_id = message.chat.id
        self.user_id = message.from_user.id
        self.full_name = message.from_user.first_name
        self.username = message.from_user.username
        self.message_id = message.id
        if SQLite(db_path).is_registered(message.chat.id):
            self.lang = SQLite(db_path).get_user_lang(self.chat_id)
