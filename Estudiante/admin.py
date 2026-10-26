from django.contrib import admin
from .models import Estudiante
# Register your models here.
@admin.register(Estudiante)
class Estudiante_admin(admin.ModelAdmin):
    list_display=('codigo','nombre','correo')
    search_fields=('codigo','correo')
