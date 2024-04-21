import os

from django.core.asgi import get_asgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trmenu.settings')

application = get_asgi_application()
