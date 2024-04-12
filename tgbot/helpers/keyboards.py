from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.texts.text_reply import *

def reply_markup(texts, row_width):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    markup.add(*texts)

    return markup


def reply_markup_with_headerbtn(texts, lang, row_width):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
    markup.add(main_header_btn[lang])
    markup.add(*texts)

    return markup


def inline_markup(texts, row_width):
    markup = InlineKeyboardMarkup(row_width=row_width)
    buttons = []
    item = 0
    for i in texts:
        button = InlineKeyboardButton(i[0], callback_data='item_'+str(item+1))
        button.append(buttons)
    markup.add(*buttons)

    return markup
