from typing import List

from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

urlpatterns: List[str] = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
]
