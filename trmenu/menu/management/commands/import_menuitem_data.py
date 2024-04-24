import csv
import sqlite3
from typing import Any

from django.core.management.base import BaseCommand  # type: ignore

from .timing import timing_decorator


class Command(BaseCommand):
    help = 'Loads deafault menu items data from csv file.'

    @timing_decorator
    def handle(self, *args: Any, **options: Any) -> None:
        with sqlite3.connect('db.sqlite3') as conn:
            cur = conn.cursor()
            print("База данных создана и успешно подключена к SQLite")
            cur.execute("CREATE TABLE IF NOT EXISTS menu_menuitem ('name', 'description', 'url', 'named_url', 'menu_id', 'parent_id');")
            with open('menu_items.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                to_db = [
                    (i['name'], i['description'], i['url'],
                     i['named_url'], i['menu_id'], i['parent_id']
                     ) for i in reader
                ]
            cur.executemany("INSERT INTO menu_menuitem ('name', 'description', 'url', 'named_url', 'menu_id', 'parent_id') VALUES (?, ?, ?, ?, ?, ?);", to_db)
            print(cur.execute('SELECT * FROM menu_menuitem').fetchall())
