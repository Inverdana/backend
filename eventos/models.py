from django.db import models
from django.core.validators import MinValueValidator

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.FileField(upload_to='arboles')
    descripcion = models.TextField(max_length=1024)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupo = models.IntegerField(validators=[MinValueValidator(1)])
    lugar = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.nombre