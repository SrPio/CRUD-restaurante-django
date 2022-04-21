from django.contrib import admin
from .models import Plato
from .models import Alimento

# Register your models here.
admin.site.register(Plato)
admin.site.register(Alimento)