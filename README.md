[# ЯП - Спринт 9 - Проект «API для Yatube». Python-разработчик (бекенд) (Яндекс.Практикум)](https://github.com/Mane26/api_final_yatube.git)

### Описание

API для Yatub представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

### Технологии

Python 3.7, Django 3.2, DRF, JWT + Djoser

### Запуск проекта в dev-режиме

- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
py -3.7 -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip

- Затем нужно установить все зависимости из файла requirements.txt
pip install -r requirements.txt

- Выполняем миграции:
python manage.py migrate

- Создаем суперпользователя:
python manage.py createsuperuser

- Запускаем проект:
python manage.py runserver

