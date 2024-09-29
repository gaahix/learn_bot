
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

web_app = InlineKeyboardMarkup(row_width=1,inline_keyboard=[[ InlineKeyboardButton(text='Приложение', web_app=WebAppInfo(url=f'https://gaahix.github.io/test_site/'))]])