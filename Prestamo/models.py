from django.db import models
from Copia_Fisica.models import Copia_Fisica
from Estudiante.models import Estudiante
from datetime import datetime,timedelta
# Create your models here.
class Prestamo(models.Model):
    copia=models.ForeignKey(Copia_Fisica,on_delete=models.PROTECT,related_name='prestamos',null=False,blank=False)
    estudiante=models.ForeignKey(Estudiante,on_delete=models.PROTECT,related_name='estudiantes',null=False,blank=False)
    fecha_prestamo=models.DateField(auto_now_add=True,null=False,blank=False)
    fecha_limite=models.DateField(null=True,blank=True)
    fecha_devolucion=models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        # Si la fecha_limite está vacía (es la primera vez que se guarda)
        if not self.fecha_limite:
            # Calculamos: fecha actual + 15 días (o el tiempo que definas)
            fecha_inicio = self.fecha_prestamo if self.fecha_prestamo else datetime.date.today()
            self.fecha_limite = self.fecha_inicio + timedelta(days=15)

        super().save(*args, **kwargs) # Guardamos el registro normalmente

    def __str__(self):
        return f"{self.copia.libro.titulo}-{self.copia.SKU}-fecha_limite{self.fecha_limite}"