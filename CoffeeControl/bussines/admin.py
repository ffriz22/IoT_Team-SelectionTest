from django.contrib import admin

# Register your models here.
from .models import Department, Worker

admin.site.register(Department)
admin.site.register(Worker)