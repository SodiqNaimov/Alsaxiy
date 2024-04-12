import sqlite3
from datetime import datetime, timedelta
import pytz
from tgbot.handlers.user import uzbekistan_timezone
from tgbot.helpers.database import *
from tgbot.files.config import db_path


def statistics_join():
    today = datetime.now(uzbekistan_timezone).date()
    one_week_ago = today - timedelta(days=7)
    one_month_ago = today - timedelta(days=30)
    db = SQLite(db_path)
    today_joins = db.get_join_stats_today(today)
    week_joins = db.get_join_stats_date_joins(one_week_ago)
    month_joins = db.get_join_stats_date_joins(one_month_ago)

    return today_joins, week_joins, month_joins

print(statistics_join())