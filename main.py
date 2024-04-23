import asyncio
import datetime

import cv2
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot("7079649833:AAEialVw6UUvAHVNa0KZua0lg5OLp8I9MfI")
chat_id = 725407118

time = datetime.datetime.now()


async def start():
    await bot.send_message(chat_id=chat_id, text=f'Пк запущен: {time}')
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()
    ret, frame = cap.read()
    cv2.imwrite('D:/Debug_utilites/cam.png', frame)
    cap.release()
    photo1 = open('D:/Debug_utilites/cam.png', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo1)


async def main():
    await bot.polling()


if __name__ == "__main__":
    asyncio.run(start())
    exit()
