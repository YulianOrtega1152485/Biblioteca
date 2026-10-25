from django.db import models
from Copia_Fisica.models import Copia_Fisica
from Estudiante.models import Estudiante
from datetime import datetime,timedelta
from django.db.models import Q
# Create your models here.
class Prestamo(models.Model):
    copia=models.ForeignKey(Copia_Fisica,on_delete=models.PROTECT,related_name='prestamos',null=False,blank=False)
    estudiante=models.ForeignKey(Estudiante,on_delete=models.PROTECT,related_name='estudiantes',null=False,blank=False)
    fecha_prestamo=models.DateField(auto_now_add=True,null=False,blank=False)
    fecha_limite=models.DateField(null=True,blank=True)
    fecha_devolucion=models.DateField(null=True,blank=True)
    
    class Meta:
        constraints=[models.UniqueConstraint(fields=['copia'],condition=Q(fecha_devolucion__isnull=True),name='unique_copia_prestada')]
    

    def clean(self):
        existe_prestamo_activo = Prestamo.objects.filter(
          copia=self.copia,
          fecha_devolucion__isnull=True
        ).exclude(pk=self.pk).exists() 
        if existe_prestamo_activo:
            raise ValidationError("Lo siento, esta copia física ya está en manos de otro estudiante.")

    def save(self, *args, **kwargs):
        self.full_clean()
        # Si la fecha_limite está vacía (es la primera vez que se guarda)
        if not self.fecha_limite:
            # Calculamos: fecha actual + 15 días (o el tiempo que definas)
            fecha_inicio = self.fecha_prestamo if self.fecha_prestamo else datetime.date.today()
            self.fecha_limite = self.fecha_inicio + timedelta(days=15)

        super().save(*args, **kwargs) # Guardamos el registro normalmente
        

    def __str__(self):
        return f"{self.copia.libro.titulo}-{self.copia.SKU}-fecha_limite{self.fecha_limite}"