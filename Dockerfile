FROM python:3.12

COPY requirements.txt /app/requirements.txt
WORKDIR /app

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование всего содержимого внутрь контейнера
COPY . .

# Установка рабочей директории для запуска
WORKDIR /app/src

# Команда запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]