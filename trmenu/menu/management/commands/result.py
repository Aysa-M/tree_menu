from typing import Any

from django.db import IntegrityError  # type: ignore


def status(func):
    def wrapper(self, *args: Any, **options: Any) -> None:
        try:
            self.stdout.write(self.style.SUCCESS(
                'Menu data successfully loaded'))
        except IntegrityError as er:
            self.stdout.write(f'{self.name} already exists in db: {er}')
    return wrapper
