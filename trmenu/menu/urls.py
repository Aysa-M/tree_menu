from typing import List

from django.urls import path  # type: ignore

from . import views

urlpatterns: List[str] = [
    path('', views.index, name='index'),
    path('<path:path>/', views.draw_menu, name='drawmenu'),
]
