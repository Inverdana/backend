from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    referido = models.ForeignKey('Usuario',on_delete=models.SET_NULL, blank=True, null=True, related_name='referidos')
    puntaje = models.IntegerField(default=0)
