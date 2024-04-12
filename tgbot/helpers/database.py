import sqlite3
# from tgbot.files.config import db_path
#
# database = sqlite3.connect(db_path)
# cursor = database.cursor()


class SQLite:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def register_user(self, user_id, language):
        with self.connection:
            self.connection.execute("""INSERT INTO users (user_id, lang) VALUES
            (?, ?)""", [user_id, language])
    def register_join_date(self, user_id, join_date):
        with self.connection:
            self.connection.execute("""INSERT INTO join_date (user_id, join_date) VALUES
            (?, ?)""", [user_id, join_date])
    def is_registered(self, user_id):
        with self.connection:
            self.cursor.execute("""SELECT user_id FROM users WHERE user_id == ? """, [user_id])
            rows = self.cursor.fetchall()

            return rows

    def get_user_lang(self, user_id):
        with self.connection:
            self.cursor.execute("""SELECT lang FROM users WHERE user_id == ? """, [user_id])
            row = self.cursor.fetchall()

            return row[0][0]

    def get_join_stats_today(self, date):
        with self.connection:
            self.cursor.execute("SELECT COUNT(*) FROM join_date WHERE join_date = ?", (date,))
            row = self.cursor.fetchone()[0]

            return row
    def get_join_stats_date_joins(self, date):
        with self.connection:
            self.cursor.execute("SELECT COUNT(*) FROM join_date WHERE join_date >= ?", (date,))
            row = self.cursor.fetchone()[0]

            return row


    def update_data_lang(self, lang, user_id):
        with self.connection:
            self.cursor.execute("""UPDATE users SET lang =? WHERE user_id = ? """, (lang, user_id))


# '''CREATE TABLE IF NOT EXISTS users
#              (user_id INTEGER PRIMARY KEY, join_date DATE)'''

# cursor.execute("""CREATE TABLE empty_cv (
#            keyboard_name_uz            text,
#            keyboard_name_ru       text,
#            place text,
#            question_uz text,
#            question_ru text
#             )
#            """)

# """
#     lang == int: 0 => uz; 1 => ru; 2 => en
# """
