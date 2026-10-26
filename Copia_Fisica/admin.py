from django.contrib import admin
from .models import Copia_Fisica

# Register your models here.
@admin.register(Copia_Fisica)
class Copia_Fisica_admin(admin.ModelAdmin):
    list_display=('SKU','libro','condicion')
    search_fields=('SKU','libro')