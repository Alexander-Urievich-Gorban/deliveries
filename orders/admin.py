from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Order

admin.site.register(Order)
