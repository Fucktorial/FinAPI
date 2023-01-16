# Базовые наброски архитектуры/бд/валидаторов

- Чтобы установить зависимости из файла requirements.txt выполните команду:
```
pip install -r requirements.txt
```

- Чтобы подключить свою бд, в файле alembic.ini меняем код ниже на путь к своей бд:
```
sqlalchemy.url = postgresql://Admin:Admin@localhost:5432/fast_api_db
```
- Аналогичная процедура в файле db.py:
```
engine = create_engine("postgresql://Admin:Admin@localhost:5432/fast_api_db")
```
- Чтобы выполнить миграцию после подключения бд, сначала выполните команду:
```
alembic revision --autogenerate -m "your message"
```
- А после этого выполните команду:
```
alembic upgrade head
```