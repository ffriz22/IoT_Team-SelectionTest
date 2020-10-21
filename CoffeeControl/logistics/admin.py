from django.contrib import admin

# Register your models here.
from .models import CoffeeType, CoffeeOrder, CoffeeStock

admin.site.register(CoffeeType)
admin.site.register(CoffeeOrder)
admin.site.register(CoffeeStock)