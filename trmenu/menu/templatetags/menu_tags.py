from typing import Dict, List

from django import template  # type: ignore
from django.core.exceptions import ObjectDoesNotExist  # type: ignore
from django.db.models.query import QuerySet  # type: ignore

from menu.models import MenuItem

register: template.Library = template.Library()


@register.inclusion_tag('includes/menu.html')
def draw_menu(menu_name: str | None = None,
              menu_item: str | None = None) -> Dict[str, str | List[str]]:
    """
    Функция - обработчик, которая из контекста получает имя объекта меню или
    пункта меню и обращается в базу данных для получения связанных с ним
    подпунктов, т.е. мы получаем здесь дочерние узлы через атрибут parent.
    Возвращает функция словарь контекста.
    """
    def get_full_menu(menu_item: str | None = None,
                      submenu: list[str] = None) -> List[str]:
        menu: List[str] = list()
        if menu_item is not None:
            menu = list(items.filter(parent__name=menu_item))
        else:
            menu = list(items.filter(parent=0))

        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass

        try:
            return get_full_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_full_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu
    items: QuerySet = MenuItem.objects.filter(menu__name=menu_name)
    return ({'menu': get_full_menu()} if menu_name == menu_item
            else {'menu': get_full_menu(menu_item)})
