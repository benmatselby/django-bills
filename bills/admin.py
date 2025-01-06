from django.contrib import admin

from .models import EnergyBill
from .models import Type
from .models import WaterBill

admin.site.register(EnergyBill)
admin.site.register(WaterBill)
admin.site.register(Type)
