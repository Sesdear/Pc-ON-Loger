# Pc_ON_Logger

Где найти данные для переменных

| `chat_id` | Нужно написать [боту](https://t.me/getmyid_bot) |
| --------- | ----------------------------------------------- |
| `bot`     | Нужно создать [Бота](https://t.me/BotFather)    |
> **Необходимые библеотеки**
1. PyTelegramBotApi
2. aiohttp
3. opencv(В случае если версия бота с камерой)
#### Настройка
1. Создаёте бота в [Ссылка](https://t.me/BotFather)
2. Копируете Токен бота
3. Вставляете токен в переменную `bot`
4. Заходите в [бота](https://t.me/getmyid_bot) и нажимаете `Старт`
5. Копируете ваш id
6. Вставляете id в переиенную `chat_id`
7. Добавляете в автозагрузку
#### Опционально
1. Скачиваете библеотеку pyinstaller
2. Отключаете антивирус (он реагирует на pyinstaller т.к. он работет как самораспаковывающийся архив )
3. Пишете в консоль: `pyinstaller --onefile <Путь к файлу бота>`
4. Нажимаете Win + R
5. Пишете: `shell:startup`
6. Перекидывайете туда ярлык от .exe файла

# *Предупреждение*
### Версия бота с камерой НЕ СКИДЫВАЕТ фото если фото находиться в системных файлах
