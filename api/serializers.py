from django.contrib.auth import get_user_model
from rest_framework import exceptions, serializers
from eventos.models import Evento
from usuarios.models import Participacion,Post
from logros.models import Logro
from drf_extra_fields.fields import Base64ImageField
from catalogo.models import Arbol, Foto

User = get_user_model()

class LogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logro
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    foto = Base64ImageField()
    class Meta:
        model = Post
        fields = '__all__'

class ParticipacionSerializer(serializers.ModelSerializer):
    evento = EventoSerializer()
    class Meta:
        model = Participacion
        fields = ('evento','asistio')   


class UsuarioYoSerializer(serializers.ModelSerializer):
    participaciones = ParticipacionSerializer(many=True)
    logros = LogroSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'email','first_name','last_name','puntaje','participaciones','logros')

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ('foto',   )

class ArbolSerializer(serializers.ModelSerializer):
    fotos = FotoSerializer(many=True)
    class Meta:
        model = Arbol
        fields = ('id','nombre','descripcion','fotos','icono')