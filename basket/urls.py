from django.urls import path
from rest_framework.routers import DefaultRouter

from basket.apps import BasketConfig
from basket.views import BasketListAPIView, BasketViewSet, ClearBasketViewSet

app_name = BasketConfig.name

router = DefaultRouter()
router.register(r"basket", BasketViewSet, basename="basket")

urlpatterns = [
    path("basket_list/", BasketListAPIView.as_view(), name="basket_list"),
    path(
        "clear/", ClearBasketViewSet.as_view({"delete": "delete"}), name="clear_basket"
    ),
] + router.urls
