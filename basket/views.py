from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.permissions import IsOwner

from .models import Basket, BasketProducts, Product
from .serializers import BasketProductsSerializer


class BasketViewSet(viewsets.ViewSet):
    """Эндпоинт операций в корзине"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_basket(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        return basket

    def create(self, request):
        basket = self.get_basket(request)
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Товар не найден."}, status=status.HTTP_404_NOT_FOUND
            )

        basket_item, created = BasketProducts.objects.get_or_create(
            basket=basket, product=product
        )

        if not created:
            basket_item.quantity += quantity
            basket_item.save()
        else:
            basket_item.quantity = quantity
            basket_item.save()

        return Response(
            BasketProductsSerializer(basket_item).data, status=status.HTTP_201_CREATED
        )

    def update(self, request, pk=None):
        basket = self.get_basket(request)
        try:
            basket_item = BasketProducts.objects.get(id=pk, basket=basket)
        except BasketProducts.DoesNotExist:
            return Response(
                {"error": "Товар в корзине не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )

        quantity = request.data.get("quantity")
        if quantity is not None:
            basket_item.quantity = quantity
            basket_item.save()

        return Response(BasketProductsSerializer(basket_item).data)

    def destroy(self, request, pk=None):
        basket = self.get_basket(request)
        try:
            basket_item = BasketProducts.objects.get(id=pk, basket=basket)
            basket_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except BasketProducts.DoesNotExist:
            return Response(
                {"error": "Товар в корзине не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )


class BasketListAPIView(generics.ListAPIView):
    """Состав корзины"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        basket, created = Basket.objects.get_or_create(user=self.request.user)
        return basket.products.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_quantity = 0
        total_price = 0.0

        products_data = []
        for item in queryset:
            product_price = item.product.price
            total_quantity += item.quantity
            total_price += product_price * item.quantity
            products_data.append(
                {
                    "id": item.id,
                    "product": item.product.title,
                    "total_quantity": item.quantity,
                    "total_price": product_price * item.quantity,
                }
            )

        response_data = {
            "products": products_data,
            "total_quantity": total_quantity,
            "total_price": total_price,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class ClearBasketViewSet(viewsets.ViewSet):
    """Очистка корзины"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        basket = Basket.objects.get(user=self.request.user)
        return basket.products.all()

    def delete(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        basket.products.all().delete()
        return Response(
            {"message": "Корзина очищена."}, status=status.HTTP_204_NO_CONTENT
        )
