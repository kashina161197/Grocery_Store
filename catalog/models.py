from django.db import models


class Category(models.Model):
    """Модель категории"""

    title = models.CharField(
        max_length=150, verbose_name="Наименование категории", unique=True
    )
    slug = models.SlugField(unique=True, verbose_name="slug-имя")
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name="Изображение"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["title"]


class Subcategory(models.Model):
    """Модель подкатегории"""

    title = models.CharField(
        max_length=150, verbose_name="Наименование подкатегории", unique=True
    )
    slug = models.SlugField(unique=True, verbose_name="slug-имя")
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories",
        verbose_name="Категория",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"
        ordering = ["title"]


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(max_length=150, verbose_name="Наименование продукта")
    slug = models.SlugField(unique=True, verbose_name="slug-имя")
    image_small = models.ImageField(
        upload_to="images/small/",
        blank=True,
        null=True,
        verbose_name="Маленькое изображение",
    )
    image_medium = models.ImageField(
        upload_to="images/medium/",
        blank=True,
        null=True,
        verbose_name="Среднее изображение",
    )
    image_large = models.ImageField(
        upload_to="images/large/",
        blank=True,
        null=True,
        verbose_name="Большое изображение",
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="Подкатегории",
        verbose_name="Подкатегория",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="Категория",
        verbose_name="Категория",
    )
    price = models.FloatField(
        help_text="Введите стоимость продукта", verbose_name="Цена"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title"]
