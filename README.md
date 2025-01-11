# Тестовое задание: Мониторинг системы

## Описание проекта
1. Отображает **загруженность CPU, RAM и диска** в реальном времени.
2. Позволяет **начать запись данных** в базу данных по нажатию кнопки.
3. В процессе записи заменяет кнопку на "Остановить" и отображает таймер.
4. После остановки записи возобновляет возможность начать новую запись.

## Структура проекта
```
.
├── db_setup.py         # Настройка базы данных PostgreSQL
├── main.py            # Основной FastAPI сервер
├── models.py          # Определение модели хранения данных
├── services.py        # Логика сбора и записи системных метрик
├── static/            # Статические файлы (HTML, CSS, JS)
│   ├── index.html
│   ├── script.js
│   └── styles.css
└── tests/             # Тесты проекта
    ├── __init__.py
    ├── conftest.py
    └── test_main.py
```

## Установка и запуск проекта
### 1. Установка зависимостей
Убедитесь, что у вас установлен **Python 3.10+** и **PostgreSQL**. Затем установите зависимости:
```sh
pip install -r requirements.txt
```

### 2. Запуск проекта
```sh
python main.py
```
Приложение запустится, и можно открыть **http://127.0.0.1:8000/** в браузере.
База данных создастся автоматически при старте сервера.

## Тестирование
Для запуска тестов используйте **pytest**:
```sh
pytest tests/
```

