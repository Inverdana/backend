from django.contrib.auth import get_user_model
from rest_framework import exceptions, serializers
from eventos.models import Evento
from usuarios.models import Participacion


User = get_user_model()

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class ParticipacionSerializer(serializers.ModelSerializer):
    evento = EventoSerializer()
    class Meta:
        model = Participacion
        fields = ('evento','asistio')   


class UsuarioYoSerializer(serializers.ModelSerializer):
    participaciones = ParticipacionSerializer(many=True)
    class Meta:
        model = User
        fields = ('email','first_name','last_name','puntaje','participaciones')