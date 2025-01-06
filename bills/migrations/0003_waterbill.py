# Generated by Django 5.1.4 on 2025-01-06 20:41

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_rename_bill_energybill'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('water_m3', models.IntegerField()),
                ('sewage_m3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estimated', models.BooleanField()),
                ('reading', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bills.type')),
            ],
        ),
    ]