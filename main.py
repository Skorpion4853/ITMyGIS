import telebot
from telebot import types
import logging
import asyncio
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os

form = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    format=form,
    datefmt='%H:%M:%S:',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

load_dotenv()
token = os.getenv("bot_token")

bot = AsyncTeleBot(token)

@bot.message_handler(commands=['start'])
async def start(message):
    try:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_top_list = types.InlineKeyboardButton('Топ 5 мест')
        btn_akinator = types.InlineKeyboardButton('Акинатор')
        btn_settings = types.InlineKeyboardButton('Настройки')
        btn_history = types.InlineKeyboardButton('История пользователя')
        markup.add(btn_top_list, btn_akinator, btn_settings, btn_history)
        await bot.send_message(
            message.chat.id,
            "Чем займёмся?",
            reply_markup=markup
        )
    except Exception as err_start:
        logger.error(f'Ошибка - {err_start}')

@bot.message_handler(commands=['help'])
async def help(message):
    try:
        help_text = "Текст о помощи"
        await bot.send_message(message.chat.id, help_text)
    except Exception as err_help:
        logger.error(f"Ошибка help'а - {err_help}")


async def main():
    print('Бот запущен!')
    await bot.polling(non_stop=True, skip_pending=True)


if __name__ == "__main__":
    asyncio.run(main())
