from django.db import models

from catalog.models import Product
from users.models import CustomsUser


class Basket(models.Model):
    """Модель корзины"""

    user = models.ForeignKey(CustomsUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "корзины"
        ordering = ["user"]


class BasketProducts(models.Model):
    """Модель корзины с товарами"""

    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE, related_name="products"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} в корзине {self.basket.user.email}"
