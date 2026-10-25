from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=120,null=False,blank=False)

    def __str__(self):
        return  self.nombre