import asyncio
import datetime

import cv2
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("Токен Бота")
chat_id = <Ваш chat_id>

time = datetime.datetime.now()


async def start():
    await bot.send_message(chat_id=chat_id, text=f'Пк запущен: {time}')


async def main():
    await start()

if __name__ == "__main__":
    asyncio.run(main())
