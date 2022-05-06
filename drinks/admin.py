# Registers Models in the Admin dashboard
from django.contrib import admin
from .models import Drink

# Register the Model here
admin.site.register(Drink)
