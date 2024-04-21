import csv
from typing import Any

from django.core.management.base import BaseCommand  # type: ignore
from django.db import IntegrityError  # type: ignore

from menu.models import MenuItem
from .result import status


class Command(BaseCommand):
    help = 'Loads deafault menu items data from csv file.'

    @status
    def handle(self, *args: Any, **options: Any) -> None:
        with open('menu_items.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(
                file,
                fieldnames=['id', 'name', 'description', 'url',
                            'named_url', 'menu_id', 'parent_id']
            )
            to_db = (MenuItem(
                name=['name'],
                description=['description'],
                parent=['parent_id'],
                url=['url'],
                named_url=['named_url'],
                menu=['menu_id']
            ) for _ in reader)
            MenuItem.objects.bulk_create(to_db)
            try:
                self.stdout.write(self.style.SUCCESS(
                    'Menu data successfully loaded'))
            except IntegrityError as er:
                self.stdout.write(f'{self.name} already exists in db: {er}')
