from django.db import models

# Create your models here.
class Estudiante(models.Model):
    codigo=models.CharField(max_length=10,unique=True,null=False,blank=False)
    nombre=models.CharField(max_length=50,null=False,blank=False)
    correo=models.CharField(max_length=150,null=False,blank=False,unique=True)

    def __str__(self):
        return f"{self.codigo}-{self.nombre}"