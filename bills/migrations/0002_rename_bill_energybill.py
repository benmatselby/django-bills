# Generated by Django 5.1.4 on 2025-01-06 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bill',
            new_name='EnergyBill',
        ),
    ]