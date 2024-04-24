from django.db import models  # type: ignore


class Menu(models.Model):
    """Creates the menu model object."""

    name = models.CharField(verbose_name='menu_title',
                            max_length=200, unique=True)
    description = models.TextField(verbose_name='menu_description',
                                   max_length=255,
                                   blank=True)

    def __str__(self) -> str:
        """Displayed a string view of the class object."""
        return self.name

    class Meta:
        """Metadata of the class"""

        ordering = ('id',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    """Creates the points of a menu model object."""

    name = models.CharField(verbose_name='item_title', max_length=200,
                            blank=False)
    description = models.TextField(verbose_name='item_description',
                                   max_length=255,
                                   blank=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='children', default=0,
                               on_delete=models.CASCADE)
    url = models.CharField(verbose_name='item_link', max_length=255,
                           blank=True)
    named_url = models.CharField(verbose_name='item_named_link',
                                 max_length=200,
                                 blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             related_name='menu_items')

    def __str__(self) -> str:
        """Displayed a string view of the class object."""
        return self.name

    class Meta:
        """Metadata of the class"""

        ordering = ('id',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
