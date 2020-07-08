from django.db import models
from django.contrib.auth.models import AbstractUser
from eventos.models import Evento
# Create your models here.
class Usuario(AbstractUser):
    referido = models.ForeignKey('Usuario',on_delete=models.SET_NULL, blank=True, null=True, related_name='referidos')
    puntaje = models.IntegerField(default=0)
    paticipaciones = models.ManyToManyField(Evento,through='Participacion')

class Participacion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='participaciones')
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    asistio = models.BooleanField(default=False)
