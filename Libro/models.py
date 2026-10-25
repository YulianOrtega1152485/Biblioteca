from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from Categoria.models import Categoria
from Autor.models import Autor
from django.db.models import Q
# Create your models here.
class Libro(models.Model):
    titulo=models.CharField(max_length=250,null=False,blank=False)
    año_publicacion=models.PositiveIntegerField(null=False,blank=False,validators=[MinValueValidator(1000),MaxValueValidator(datetime.date.today().year+1)])
    ISBN=models.CharField(max_length=17,null=True,blank=True,unique=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT,related_name='Libros',null=False,blank=False)
    autores= models.ManyToManyField(Autor,related_name='libros')
    idioma=models.CharField(max_length=20,null=False,blank=False)
    class Meta:
         constraints = [
            models.CheckConstraint(condition=Q(año_publicacion__gte=1000),name='check_anio_publicacion_minimo'),
            models.CheckConstraint(condition=Q(año_publicacion__lte=datetime.date.today().year),name='check_anio_publicacion_maximo'),
        ]

 
    def __str__(self):
        return f"{self.titulo}({self.año_publicacion})"

    