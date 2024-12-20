from django.contrib import admin

from .models import Bill, Type

admin.site.register(Bill)
admin.site.register(Type)
