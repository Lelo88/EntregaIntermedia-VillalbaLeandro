from django.contrib import admin
from .models import Libro, Sector, Lector

# Register your models here.
admin.site.register(Libro)
admin.site.register(Sector)
admin.site.register(Lector)