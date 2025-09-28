from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта')
    image = models.ImageField(upload_to='catalog/image', verbose_name='Изображение', help_text='Загрузите изображение продукта', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену продукта')
    created_at = models.DateField(verbose_name='Дата создания', help_text='Введите дату создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения', help_text='Введите дату последнего изменения')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name','price']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name', 'price']
