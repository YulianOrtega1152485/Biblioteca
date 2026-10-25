from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from Categoria.models import Categoria
# Create your models here.
class Libro(models.Model):
    titulo=models.CharField(max_length=250,null=False,blank=False)
    año_publicacion=models.PositiveIntegerField(null=False,blank=False,validators=[MinValueValidator(1000),MaxValueValidator(datetime.date.today().year+1)])
    ISBN=models.CharField(max_length=17,null=True,blank=True,unique=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT,related_name='Libros',null=False,blank=False)

    def __str__(self):
        return f"{self.titulo}({self.año_publicacion})"