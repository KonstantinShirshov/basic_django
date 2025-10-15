from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    content = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое"
    )
    preview = models.ImageField(
        upload_to="images/",
        verbose_name="Превью",
        help_text="Загрузите превью статьи",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    publication_sign = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Cчетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["title", "created_at"]