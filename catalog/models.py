from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ]
