from datetime import date

from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    category_name = models.CharField(
        max_length=100, verbose_name='Наименование')
    category_description = models.CharField(
        max_length=250, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name', )


class Product(models.Model):

    product_name = models.CharField(
        max_length=150, verbose_name='Наименование')
    product_description = models.CharField(
        max_length=250, verbose_name='Описание')
    product_image = models.ImageField(
        upload_to='catalog/',
        default='catalog/default_image.jpeg',
        max_length=150,
        verbose_name='Изображение(превью)',
        **NULLABLE
    )
    product_category_name = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')
    product_sale_price = models.FloatField(verbose_name='Цена за штуку')
    create_date = models.DateField(
        verbose_name='Дата создания', default=date.today())
    update_date = models.DateField(
        verbose_name='Дата последнего изменения', default=date.today())

    def __str__(self):
        return f'{self.product_name} {self.product_sale_price} {self.product_category_name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('product_name', )
