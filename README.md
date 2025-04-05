# Telegram Stories Liker App

## Описание
Этот проект — асинхронный бот для Telegram, который автоматически ставит реакции (❤️) на сторис пользователей из списка диалогов. Реакции отправляются с ограничением: не чаще одного раза в 2 дня для каждого пользователя. Данные о пользователях и времени последнего лайка хранятся в базе данных PostgreSQL с использованием SQLAlchemy и миграций Alembic.

## Требования
- Python 3.10 или выше
- PostgreSQL 13+
- Зависимости (см. `requirements.txt`)


## Установка

1. **Клонируйте репозиторий**:
 ```bash
 git clone https://github.com/usatore/tg-stories-liker
 cd telegram-stories-liker
 ```

2. **Создайте и активируйте виртуальное окружение**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Установите зависимости**:
```bash
pip install -r requirements.txt
```

4. **Настройте Telegram API**:

Получите **api_id** и **api_hash** на my.telegram.org.

5. **Запуск приложения**:

После того как вы настроили все зависимости и переменные окружения, вы можете запустить приложение.

Для запуска с использованием Docker Compose:
```bash
  docker-compose up --build






