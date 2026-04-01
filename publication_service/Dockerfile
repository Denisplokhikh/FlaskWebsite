FROM python:3.11-slim

WORKDIR /app

# копируем зависимости
COPY requirements.txt .

# ставим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# копируем проект
COPY . .

# порт Flask
EXPOSE 5002

# запуск
CMD ["python", "app.py"]