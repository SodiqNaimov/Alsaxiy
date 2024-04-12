import telebot
from telebot import custom_filters
from telebot.storage import StateMemoryStorage

from tgbot.files.config import token
from tgbot.handlers.user import *
from tgbot.handlers.admin import *
state_storage = StateMemoryStorage()
bot = telebot.TeleBot(token, state_storage=state_storage, parse_mode='HTML')

# To shorten the "register_message_handler" code
def register_m_handler(func, text, state, commands):
    return bot.register_message_handler(func, text=text, state=state, commands=commands, pass_bot=True)



def register_handlers():
    register_m_handler(start, None, None, ['start'])
    # For choose language
    register_m_handler(language, lang_btn, MyStates.start, None)

    # For settings
    register_m_handler(user_settings, ["⚙️Sozlamalar", "⚙️ Настройки"],  MyStates.headers_st, None)
    register_m_handler(headers, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.settings_st, None)

    # update language
    register_m_handler(user_language, ["🌐 Tilni tanlash", "🌐 Выбрать язык", "🌐 Choose a language"], MyStates.settings_st,
                       None)
    register_m_handler(update_language, ["🇺🇿O'zbek tili", "🇷🇺Pусский язык", "🇺🇸 English"], MyStates.update_language,
                       None)
    # For about company
    register_m_handler(about_company, ["🚀 Biz haqimizda", "🚀 О нас"],  MyStates.headers_st, None)
    # For all cv
    register_m_handler(all_cv_funct, ["🧾 Barcha vakansiyalar", "🧾 Все вакансии"],  MyStates.headers_st, None)
    register_m_handler(headers, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_cv_funct_st, None)
    # For all cv 2 - stage
    register_m_handler(all_cv_funct_second_stage, ["2-qavat", "2-й этаж"], MyStates.all_cv_funct_st, None)
    register_m_handler(all_cv_funct, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_cv_funct_second_stage_st, None)

    # For all cv 1 - stage
    register_m_handler(all_cv_funct_first_stage, ["1-qavat", "1-й этаж"], MyStates.all_cv_funct_st, None)
    register_m_handler(all_cv_funct, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_cv_funct_first_stage_st, None)
    register_m_handler(all_cv_first_stage_office, ["🏣 Office", "🏣 Офис"], MyStates.all_cv_funct_first_stage_st, None)
    register_m_handler(all_cv_funct_first_stage, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_cv_first_stage_office_st, None)
    register_m_handler(all_cv_first_stage_zal, ["🏤 Zal", "🏤 Зал"], MyStates.all_cv_funct_first_stage_st, None)
    register_m_handler(all_cv_first_stage_zal, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_cv_first_stage_office_st, None)

    # For all shop
    register_m_handler(all_shops, ["📍 Barcha do'konlarimiz",  "📍 Все наши магазины"], MyStates.headers_st, None)
    register_m_handler(headers, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_shops_st, None)
    register_m_handler(all_shop_jobs, list_of_allshop_btn, MyStates.all_shops_st, None)
    register_m_handler(all_shops, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.all_shop_jobs_st, None)

    # For empty cv
    register_m_handler(empty_vacation_func, ["💼 Bo'sh ish o'rinlari", "💼 Пустый Вакансии"],  MyStates.headers_st, None)
    register_m_handler(headers, ["⬅️ Ortga", "⬅️ Назад"],  MyStates.empty_vacation_func_st, None)



    # For all back to header
    register_m_handler(headers, ["🏠 Bosh sahifa", "🏠 Главное страница"], "*", None)


# function that returns all sentences with the same meaning
def lang_texts(list, text_index):
    texts = []
    # if text_index is -1, it returns all sentences in the list
    if text_index == -1:
        return [elem for sublist in list for elem in sublist]

    for k in list:
        texts.append(k[text_index])
    return texts


def run():
    bot.infinity_polling(skip_pending=True)


register_handlers()

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.IsDigitFilter())
run()
