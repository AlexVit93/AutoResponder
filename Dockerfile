# Используем официальный образ Python 3.12.2
FROM python:3.12.2-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY . .

ENV PYTHONUNBUFFERED=1

# Команда, которая запускается при старте контейнера
CMD ["python", "main.py"]


