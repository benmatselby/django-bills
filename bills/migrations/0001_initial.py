# Generated by Django 5.1.4 on 2024-12-20 19:56

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Type",
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
                ("handle", models.CharField(max_length=200, unique=True)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Bill",
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
                ("date_start", models.DateField()),
                ("date_end", models.DateField()),
                ("units_kwh", models.IntegerField()),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("estimated", models.BooleanField()),
                ("reading", models.IntegerField()),
                ("comments", models.CharField(max_length=200)),
                (
                    "type",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bills.type",
                    ),
                ),
            ],
        ),
    ]
