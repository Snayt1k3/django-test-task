from django.db import models

# Create your models here.


class TreeMenuCategory(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField('Name', max_length=255, blank=True, null=False)
    verbose_name = models.CharField('Verbose name', max_length=255, blank=True, null=False)

    def __str__(self):
        return self.verbose_name


class TreeMenu(models.Model):

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    name = models.CharField("Name", max_length=255, blank=True, null=False)

    category = models.ForeignKey(
        TreeMenuCategory,
        verbose_name='Category',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField('Link or Named Url', max_length=1000, blank=True, null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name='Parent element',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name
