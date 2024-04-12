import sqlite3
import pytz
from telebot import TeleBot
from telebot.types import Message  # ReplyKeyboardRemove, CallbackQuery
from datetime import datetime, timedelta
# for get user info
from tgbot.helpers.user_information import User_info

# for state
from tgbot.states.state import MyStates

# messages
from tgbot.texts.messages import *

# for use keyboards
from tgbot.helpers.keyboards import *  # , inline_markup
from tgbot.texts.text_reply import *

# for use database
from tgbot.helpers.database import SQLite
from tgbot.files.config import db_path

# Define Uzbekistan timezone
uzbekistan_timezone = pytz.timezone('Asia/Tashkent')


def start(message: Message, bot: TeleBot):
    print('start')
    db = SQLite(db_path)
    rows = db.is_registered(message.from_user.id)
    if len(rows) == 0:
        btn = reply_markup(lang_btn, 2)  # 0 => user.lang
        bot.send_message(message.chat.id, msg_start.format(message.from_user.first_name, message.from_user.first_name),
                         reply_markup=btn)
        bot.set_state(message.from_user.id, MyStates.start, message.chat.id)
    else:
        headers(message, bot)


def language(message: Message, bot: TeleBot):
    db = SQLite(db_path)
    join_date = datetime.now(uzbekistan_timezone).date().isoformat()
    # print(join_date)
    if message.text in lang_btn:
        if message.text == lang_btn[1]:
            db.register_user(message.chat.id, 'ru')
        if message.text == lang_btn[0]:
            db.register_user(message.chat.id, 'uz')
        db.register_join_date(message.chat.id, join_date)

    headers(message, bot)


def headers(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, header_example[user.lang], reply_markup=reply_markup(headers_btn[user.lang], 2))
    bot.set_state(message.from_user.id, MyStates.headers_st, message.chat.id)


def empty_vacation_func(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, empty_cv_message[user.lang], reply_markup=reply_markup(empty_cv_btn[user.lang], 2))
    bot.set_state(message.from_user.id, MyStates.empty_vacation_func_st, message.chat.id)




def all_shops(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, all_shop_message[user.lang], reply_markup=reply_markup(all_shop_btn[user.lang], 2))
    bot.set_state(message.from_user.id, MyStates.all_shops_st, message.chat.id)


def all_shop_jobs(message: Message, bot: TeleBot):
    user = User_info(message)
    if message.text in ["🍞 Al-sahiy non (novvoyxona)", "🍞 Al-sahiy хлеб (пекарня)"]:
        reply_btn_name = [all_shop_jobs_btn[user.lang][0], all_shop_jobs_btn[user.lang][2],
                          all_shop_jobs_btn[user.lang][3], main_header_btn[user.lang]]
        markup = reply_markup(reply_btn_name,  2)
    elif message.text == "💰 Paynet":
        reply_btn_name = [all_shop_jobs_btn[user.lang][1], all_shop_jobs_btn[user.lang][3], main_header_btn[user.lang]]
        markup = reply_markup(reply_btn_name,  1)
    else:
        reply_btn_name = [all_shop_jobs_btn[user.lang][0], all_shop_jobs_btn[user.lang][3], main_header_btn[user.lang]]
        markup = reply_markup(reply_btn_name, 1)

    bot.send_message(message.chat.id, all_shop_message[user.lang],
                     reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.all_shop_jobs_st, message.chat.id)
def all_cv_funct(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, all_cv_funct_message[user.lang],
                     reply_markup=reply_markup(all_cv_btn[user.lang], 2))
    bot.set_state(message.from_user.id, MyStates.all_cv_funct_st, message.chat.id)


# Second Stage
def all_cv_funct_second_stage(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, all_cv_funct_second_stage_message[user.lang],
                     reply_markup=reply_markup_with_headerbtn(all_cv_second_stage_btn[user.lang], user.lang, 2))
    bot.set_state(message.from_user.id, MyStates.all_cv_funct_second_stage_st, message.chat.id)


# First Stage
def all_cv_funct_first_stage(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, all_cv_funct_first_stage_message[user.lang],
                     reply_markup=reply_markup_with_headerbtn(all_cv_first_stage_btn[user.lang], user.lang, 2))
    bot.set_state(message.from_user.id, MyStates.all_cv_funct_first_stage_st, message.chat.id)


def all_cv_first_stage_office(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, header_example[user.lang],
                     reply_markup=reply_markup_with_headerbtn(all_cv_first_stage_office_btn[user.lang], user.lang, 2))
    bot.set_state(message.from_user.id, MyStates.all_cv_first_stage_office_st, message.chat.id)


def all_cv_first_stage_zal(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, header_example[user.lang],
                     reply_markup=reply_markup_with_headerbtn(all_cv_first_stage_zal_btn[user.lang], user.lang, 2))
    bot.set_state(message.from_user.id, MyStates.all_cv_first_stage_office_st, message.chat.id)


# About Company
def about_company(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, about_company_message[user.lang])
    headers(message, bot)


# For setting
def user_settings(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, settings_message[user.lang],
                     reply_markup=reply_markup(settings_button[user.lang], 2))
    bot.set_state(message.from_user.id, MyStates.settings_st, message.chat.id)


def user_language(message: Message, bot: TeleBot):
    user = User_info(message)
    bot.send_message(message.chat.id, update_language_message[user.lang], reply_markup=reply_markup(lang_btn, 2))
    bot.set_state(message.from_user.id, MyStates.update_language, message.chat.id)


def update_language(message: Message, bot: TeleBot):
    db = SQLite(db_path)
    if message.text in lang_btn:
        if message.text == lang_btn[1]:
            db.update_data_lang("ru", message.chat.id)
        if message.text == lang_btn[0]:
            db.update_data_lang("uz", message.chat.id)
    headers(message, bot)
