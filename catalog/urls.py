from rest_framework.routers import DefaultRouter

from catalog.apps import CatalogConfig
from catalog.views import CategoryViewSet, ProductViewSet

app_name = CatalogConfig.name

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [] + router.urls
