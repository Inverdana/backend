from django.db import models

# Create your models here.
class Logro(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=255)
    foto = models.ImageField()
    