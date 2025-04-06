from rest_framework import serializers

from .models import Basket, BasketProducts


class BasketSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины"""

    class Meta:
        model = Basket
        fields = "__all__"


class BasketProductsSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины с продуктами"""

    class Meta:
        model = BasketProducts
        fields = ["id", "product", "quantity"]
