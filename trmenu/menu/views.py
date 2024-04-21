from typing import Dict, List

from django.shortcuts import render  # type: ignore

from .models import Menu


def index(request) -> None:
    """
    Функция - обработчик, которая выводит имеющиеся главные меню.
    Выводит домашнюю стартовую страницу с объектами меню.
    """
    menus: Menu = Menu.objects.all()
    context: Dict[str, str] = {'menus': menus}
    return render(request, 'index.html', context)


def draw_menu(request, path) -> None:
    """
    Функция - обработчик, из которой получаем контекст для дальнейшей
    отрисовки пунктов выбранного меню.
    """
    if path:
        path_els: List[str] = path.split('/')
        menu_name, menu_item = path_els[0], path_els[-1]
        context: Dict[str, str] = {
            'menu_name': menu_name,
            'menu_item': menu_item
        }
    return render(request, 'index.html', context)
