from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Constraints)
class ConstraintAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Constraints._meta.get_fields()]
