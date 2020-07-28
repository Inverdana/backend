from django.shortcuts import render
from rest_framework import generics, status, views, viewsets
from .serializers import EventoSerializer,PostSerializer,ArbolSerializer
from eventos.models import Evento
from usuarios.models import Participacion,Usuario,Post
from rest_framework.decorators import action
from rest_framework.response import Response
from catalogo.models import Arbol

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
            participantes_actuales = len(Participacion.objects.filter(evento=pk))
            if participantes_actuales>=evento.cupo:
                return Response(status=status.HTTP_410_GONE)
            Participacion(evento=evento,usuario=request.user).save()
        return Response(status=status.HTTP_201_CREATED)

    @action(["delete"], detail=True)
    def desinscribirse(self, request, pk=None):
        try:
            Participacion.objects.get(evento=pk,usuario=request.user).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Participacion.DoesNotExist:
            pass
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def create(self, request, *args, **kwargs):
        user = self.request.user
        request.data['usuario'] = user.id
        return super().create(request,args,kwargs)

class ArbolesCatalogoViewSet(viewsets.ModelViewSet):
    serializer_class = ArbolSerializer
    queryset = Arbol.objects.all()