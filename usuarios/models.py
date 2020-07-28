from django.db import models
from django.contrib.auth.models import AbstractUser
from eventos.models import Evento
from logros.models import Logro
# Create your models here.
class Usuario(AbstractUser):
    referido = models.ForeignKey('Usuario',on_delete=models.SET_NULL, blank=True, null=True, related_name='referidos')
    puntaje = models.IntegerField(default=0)
    paticipaciones = models.ManyToManyField(Evento,through='Participacion')
    logros = models.ManyToManyField(Logro,through='UsuarioLogro')
class Participacion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='participaciones')
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    asistio = models.BooleanField(default=False)

class UsuarioLogro(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    logro = models.ForeignKey(Logro, on_delete=models.CASCADE)

class Post(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    foto =  models.ImageField(upload_to='posts',null=True,blank=True)
