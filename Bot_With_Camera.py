import asyncio
import datetime

import cv2
from telebot.async_telebot import AsyncTeleBot
########################################################
### Переменные
bot = AsyncTeleBot("Токен Бота")
chat_id = <Ваш chat_id>
########################################################
    
time = datetime.datetime.now()


async def start():
    await bot.send_message(chat_id=chat_id, text=f'Пк запущен: {time}')
    cap = cv2.VideoCapture(0)
    for i in range(30):
        cap.read()
    ret, frame = cap.read()
    cv2.imwrite('cam.png', frame)
    cap.release()
    photo1 = open('cam.png', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo1)


async def main():
    await start()

if __name__ == "__main__":
    asyncio.run(main())
