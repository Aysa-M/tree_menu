import os
from typing import Any

from django.contrib.auth import get_user_model  # type: ignore
from django.core.management.base import BaseCommand  # type: ignore
from dotenv import load_dotenv

from .timing import timing_decorator

load_dotenv()

SUPER_NAME = os.getenv('SUPER_NAME', default='superadmin')
SUPER_EMAIL = os.getenv('SUPER_EMAIL', default='superadmin@mail.ru')
SUPER_PASS = os.getenv('SUPER_PASS', default='superadmin_pPASS')

USER = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser.'
    User = USER

    @timing_decorator
    def handle(self, *args: Any, **options: Any) -> None:
        """
        Создание суперпользователя с параметрами, хранящимися в файле .env
        либо со значениями по умолчанию.
        """
        self.User.objects.create_superuser(
            username=SUPER_NAME,
            email=SUPER_EMAIL,
            password=SUPER_PASS)
        self.stdout.write(self.style.SUCCESS(
            'Superuser successfully created.'))
