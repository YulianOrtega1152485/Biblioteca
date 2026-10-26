from django.contrib import admin
from .models import Autor
# Register your models here.


@admin.register(Autor)
class Autor_admin(admin.ModelAdmin):
    list_display=('id','nombre')
    search_fields=('nombre',)