from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from catalog.models import Category, Product
from catalog.paginators import ADSPagination
from catalog.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """Список категорий"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ADSPagination
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ViewSet):
    """Список продуктов"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ADSPagination
    permission_classes = [IsAuthenticated]
