from django.db import models


class Type(models.Model):
    handle = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)


class Bill(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, default=1)
    date_start = models.DateField()
    date_end = models.DateField()
    units_kwh = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated = models.BooleanField()
    reading = models.IntegerField()
    comments = models.CharField(max_length=200)
