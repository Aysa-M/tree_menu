# tree_menu
Django application implementing tree liked menu.

## Технологии (основные инструменты): ##
Python==3.11.9
Django==5.0.4

# Последовательность команд для запуска проекта:

1. Клонируйте репозиторий: $ git clone https://github.com/Aysa-M/tree_menu.git

2. Создайте виртуальное окружение (venv) - должен быть флажок в начале строки: $ python -m venv venv

3. Активируйте виртуальное окружение (venv): $ source venv/Scripts/activate

4. Установите зависимости: $ pip install -r requirements.txt

5. Сделайте миграции моделей в БД:
5.1. Нужно перейти в директорию с файлом управления проекта - /c/Dev/tree_menu/trmenu
*python manage.py makemigrations*
*python manage.py migrate*

6. Заполните БД тестовыми данными:

6.1. Создать суперпользователя для работы в admin Django:
*python manage.py create_superuser*

6.2. Загрузить данные из csv файлов:
*python manage.py import_menu_data* - загрузка данных модели Menu
*python manage.py import_menuitem_data* - загрузка данных модели MenuItem

7. Запустить учебный сервер для проверки отображения:
*python manage.py runserver*

URLs проекта:

Сайт http://127.0.0.1:8000/<наименование меню / пункта меню по мере перехода по пунктам>
Административный портал доступен по адресу http://127.0.0.1:8000/admin/

## Автор:
## Matsakova Aysa