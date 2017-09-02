from django.contrib import admin

from .models import Purchase
from .models import Items

admin.site.register(Purchase)
admin.site.register(Items)
