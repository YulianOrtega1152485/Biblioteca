from django.db import models

# Create your models here.

class Categoria(models.Model):
    descripcion=models.CharField(max_length=20,null=False,blank=False,unique=True)

    def __str__(self):
        return self.descripcion