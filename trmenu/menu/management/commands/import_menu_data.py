import csv
from typing import Any

from django.core.management.base import BaseCommand  # type: ignore
from django.db import IntegrityError  # type: ignore

from menu.models import Menu
from .timing import timing_decorator


class Command(BaseCommand):
    help = 'Loads deafault menus data from csv file.'

    @timing_decorator
    def handle(self, *args: Any, **options: Any) -> None:
        with open('menus.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(
                file,
                delimiter=',',
                fieldnames=['name', 'description']
            )
            to_db = (Menu(
                name=_['name'],
                description=_['description']
            ) for _ in reader)
            Menu.objects.bulk_create(to_db)
            try:
                self.stdout.write(self.style.SUCCESS(
                    'Menu data successfully loaded'))
            except IntegrityError as er:
                self.stdout.write(f'{self.name} already exists in db: {er}')
