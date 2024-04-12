from telebot.handler_backends import State, StatesGroup  # States


class MyStates(StatesGroup):
    start = State()
    lang = State()
    headers_st = State()
    settings_st = State()
    update_language = State()
    all_cv_funct_st = State()
    all_cv_funct_second_stage_st = State()
    all_cv_funct_first_stage_st = State()
    all_cv_first_stage_office_st = State()
    all_shops_st = State()
    all_shop_jobs_st = State()
    empty_vacation_func_st = State()
    # lang = State