from django.db import models

##
# Can we not have one type, with a field for gas/electricity?
##

class Gas(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    units_kwh = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated = models.BooleanField()
    reading = models.IntegerField()
    comments = models.CharField(max_length=200)

class Electricity(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    units_kwh = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated = models.BooleanField()
    reading = models.IntegerField()
    comments = models.CharField(max_length=200)


# from django.utils import timezone
# from bills.models import Gas
# g = Gas(date_start=timezone.now(), date_end=timezone.now(), units_kwh=100, cost=100, estimated=False, reading=100, comments="test")
# g.save()
