# Generated by Django 5.2 on 2025-04-05 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basket", "0001_initial"),
        ("catalog", "0005_alter_subcategory_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basket",
            name="products",
        ),
        migrations.RemoveField(
            model_name="basket",
            name="quantity",
        ),
        migrations.CreateModel(
            name="BasketProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "basket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="basket.basket",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
        ),
    ]
