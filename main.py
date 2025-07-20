from telebot import types
import logging
import asyncio
from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv
import os

from AIMethods import akinator
from DataBaseMethods import add_user

# from DataBaseMethods import *


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
token = os.getenv("BOT_TOKEN")

bot = AsyncTeleBot(token)


@bot.message_handler(commands=['start'])
async def start(message):
    try:
        user_id = message.from_user.id
        markup_city = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup_city.add(types.KeyboardButton('Новосибирск'))
        markup_city.add(types.KeyboardButton('Москва'))
        markup_city.add(types.KeyboardButton('Санкт-Петербург'))

        await bot.send_message(
            message.chat.id,
            "👋 Привет! Для вашего удобства и безопасности мы определяем ваш ID в Telegram. "
            "Подскажите, пожалуйста, ваш город в котором вы проживаете! 😊",
            reply_markup=markup_city
        )

    except Exception as err_start:
        logger.error(f'Ошибка в start - {err_start}')


@bot.message_handler(func=lambda message: message.text in ['Новосибирск', 'Москва', 'Санкт-Петербург'])
async def handle_city(message):
    try:
        user_id = message.from_user.id
        city = message.text
        cities = {'Новосибирск': 1, 'Москва':2, 'Санкт-Петербург':3}
        add_user(user_id, cities[city])

        markup_remove = types.ReplyKeyboardRemove()
        await bot.send_message(
            message.chat.id,
            f"Отлично, спасибо!☺️\nВаш город {city}. Записали!📝",
            reply_markup=markup_remove
        )
        markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_top_list = types.KeyboardButton('Топ 5 мест')
        btn_akinator = types.KeyboardButton('Акинатор')
        btn_settings = types.KeyboardButton('Настройки')
        btn_history = types.KeyboardButton('История пользователя')
        markup_main.add(btn_top_list, btn_akinator, btn_settings, btn_history)

        await bot.send_message(
        message.chat.id,
        "Чем займёмся?",
        reply_markup=markup_main
        )

    except Exception as err_city:
        logger.error(f'Ошибка при обработке города - {err_city}')

@bot.message_handler(commands=['help'])
async def help(message):
    try:
        help_text = """
        ✨ Помощь по боту
Я помогу найти интересные места вокруг! Вот что умею:  

🦊 Акинатор
Подберёт идеальное место для отдыха сегодня в вашем городе  

⭐ Рейтинг
Покажет топовые места:  
→ Самые популярные за сегодня
→ Лучшие за месяц

⚙️ Настройки
Смените город для поиска локаций  

📜 История
Ваши 5 последних найденных мест  

🔙 Возврат
Отменит предыдущее действие  

Просто выберите нужный раздел в меню ↓
        """
        await bot.send_message(message.chat.id, help_text)
    except Exception as err_help:
        logger.error(f"Ошибка help'а - {err_help}")

@bot.message_handler(func=lambda message: message.text in ['Акинатор'])
async def handle_city(message):
    try:
        msg = message.text
        if msg not in ['1', '2', '3', 'ничего']:
            a, l = akinator(msg, 1, [])
            await bot.send_message(message.chat.id, a)
        else:
            a, l = akinator(msg, 1, l)
            await bot.send_message(message.chat.id, a)
    except:
        await bot.send_message(message.chat.id, "что-то не работает, но мы это обязательно починим")


async def main():
    print('Бот запущен!')
    await bot.polling(non_stop=True, skip_pending=True)


if __name__ == "__main__":
    asyncio.run(main())
