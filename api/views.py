from django.shortcuts import render
from rest_framework import generics, status, views, viewsets
from .serializers import EventoSerializer
from eventos.models import Evento
from usuarios.models import Participacion,Usuario
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class EventosViewSet(viewsets.ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    @action(["post"], detail=True)
    def inscribirse(self, request, pk=None):
        try:
            Participacion.objects.get(evento=pk,usuario=request.user)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        except Participacion.DoesNotExist:
            evento = Evento.objects.get(pk=pk)
            Participacion(evento=evento,usuario=request.user).save()
        return Response(status=status.HTTP_201_CREATED)