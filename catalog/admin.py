from django.contrib import admin

from .models import Category, Product, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "image")


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "image", "category")
    list_filter = ("category",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "price",
        "subcategory",
        "category",
        "image_small",
        "image_medium",
        "image_large",
    )
    list_filter = ("subcategory", "category")
