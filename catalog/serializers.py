from rest_framework import serializers

from catalog.models import Category, Product, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для подкатегории"""

    class Meta:
        model = Subcategory
        fields = ("title", "slug", "image")


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории"""

    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("title", "slug", "image", "subcategories")


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра одного продукта"""

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "slug",
            "price",
            "category",
            "subcategory",
            "image_small",
            "image_medium",
            "image_large",
        )
