from django.db import models

# Create your models here.
class Arbol(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=1024)
    icono = models.FileField(upload_to='arboles')
    class Meta:
        verbose_name_plural = "Árboles"
    def __str__(self):
        return "%s" % self.nombre
class Foto(models.Model):
    arbol = models.ForeignKey(Arbol,related_name='fotos', on_delete=models.CASCADE)
    foto = models.FileField(upload_to='arboles')
    class Meta:
        verbose_name_plural = "Fotos"
