# Generated by Django 5.1.4 on 2025-01-11 17:06

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_waterbill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energybill',
            name='reading',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='energybill',
            name='units_kwh',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='waterbill',
            name='reading',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='waterbill',
            name='water_m3',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
