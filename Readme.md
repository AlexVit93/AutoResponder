## Автоотчетик на Pyrogram

Автоответчик, позволяющий отвечать на сообщения других пользователей, когда вы заняты.

### Первая установка.

0. Получите API ID и API Hash: Эти данные можно получить через сайт [my.telegram.org](https://my.telegram.org/auth). Залогиньтесь с вашим личным аккаунтом, создайте новое приложение и получите API ID и API Hash. Добавьте ваши API ID и API Hash в файл .env(надо предварительно создать)

1. Локально создайте файл сессии:

Запустите этот скрипт локально, где вы сможете ввести номер телефона и код подтверждения:

```python
from pyrogram import Client
from decouple import config

API_ID = config("API_ID")
API_HASH = config("API_HASH")

app = Client("my_account_session", api_id=API_ID, api_hash=API_HASH)

app.start()
app.stop()
```

Этот скрипт создаст файл сессии my_account_session.session.

2. Перенесите файл сессии на сервер: Загрузите созданный файл my_account_session.session на ваш сервер или хостинг, где будет работать ваш бот.

3. Уберите app.start() и app.stop() из кода и добавьте следующую часть кода для автоответчика:

```python

# Настраиваем часы доступности
start_hour = 14 # рабочее время (со скольки)
end_hour = 1  # До 1:59 включительно (следующего дня)
timezone_offset = 3  # UTC+3 (ваш часовой пояс тут)

@app.on_message(filters.private)
async def auto_response(client, message):
    now = datetime.now(timezone.utc)
    local_time = now + timedelta(hours=timezone_offset)
    now_hour = local_time.hour
    now_weekday = local_time.weekday()  # 0 - Понедельник, 6 - Воскресенье

    if (now_hour >= end_hour and now_hour < start_hour) or now_weekday in [5, 6]:  # Проверяем нерабочее время
        await message.reply_text("Извините, я сейчас недоступен. Пожалуйста, свяжитесь со мной с 14:00 до 01:00 по UTC+3 в будние дни.")
    else:
        await message.reply_text("Спасибо за ваше сообщение. Я постараюсь ответить вам как можно скорее!")

if __name__ == "__main__":
    print("Bot is running...")
    app.run()  # Это запускает polling, который обрабатывает обновления в режиме реального времени

```

4. Загружаем на сервер все файлы (my_account_session.session, .env(с данными от https://my.telegram.org/auth), Procfile, main.py, requirements.txt, Readme и Dockerfile для сборки в контейнере) и пользуемся!
