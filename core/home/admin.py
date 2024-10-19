from django.contrib import admin

# Register your models here.
from .models import Receipe, Ingredients

admin.site.register(Receipe)
admin.site.register(Ingredients)
