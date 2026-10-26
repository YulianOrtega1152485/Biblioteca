from django.contrib import admin
from .models import Categoria
# Register your models here.

@admin.register(Categoria)
class Categoria_admin(admin.ModelAdmin):
    list_display=('id','descripcion')