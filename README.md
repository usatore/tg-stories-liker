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
    ```

## Описание работы с фоновыми задачами

В этом проекте используется библиотека **APScheduler** для автоматического выполнения фоновых задач. Каждые 30 минут бот проверяет сторис всех пользователей из списка диалогов и ставит реакцию (❤️), если это не было сделано в последние 2 суток. Если реакция уже была поставлена, бот пропускает этого пользователя.

### Сценарий работы с лайками:
1. **Каждые 30 минут** запускается задача, которая перебирает всех пользователей.
2. Для каждого пользователя проверяется, был ли поставлен лайк за последние 2 дня.
3. Если лайк был поставлен, пользователь пропускается.
4. В противном случае, ставится лайк на всех сторис пользователя.

### Требования к базе данных:
- Для хранения информации о последнем лайке каждого пользователя используется таблица в PostgreSQL.
- Время каждого лайка записывается в БД.

## Примечания:
- Если вы хотите изменить частоту выполнения задач, настройте параметр интервала в **APScheduler**.



