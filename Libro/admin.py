from django.contrib import admin
from .models import Libro
from Copia_Fisica.models import Copia_Fisica

# Register your models here.
class Copia_fisica_inline(admin.TabularInline):
    model=Copia_Fisica
    extra=1

@admin.register(Libro)
class Libro_admin(admin.ModelAdmin):
    list_display=('titulo','año_publicacion','idioma','categoria')
    search_fields=('titulo','ISBN')
    list_editable=('idioma',)
    inline=[Copia_fisica_inline]
