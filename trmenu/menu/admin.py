from django.contrib import admin  # type: ignore

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    list_filter = ('name',)
    ordering = ('id',)
    empty_value_display = '--empty--'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'menu',)
    list_editable = ('name', 'parent', 'menu',)
    search_fields = ('name', 'parent', 'menu',)
    list_filter = ('name', 'parent', 'menu',)
    ordering = ('parent', 'menu', 'pk',)
    empty_value_display = '--empty--'
