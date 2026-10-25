from django.db import models
from Libro.models import Libro
# Create your models here.
class Copia_Fisica(models.Model):
    SKU=models.CharField(max_length=50,null=False,blank=False,unique=True)
    condicion=models.TextField(null=False,blank=False)
    libro=models.ForeignKey(Libro,on_delete=models.PROTECT,related_name='copias',null=False,blank=False)

    def __str__(self):
        return f"{self.libro.titulo}-{self.SKU}"