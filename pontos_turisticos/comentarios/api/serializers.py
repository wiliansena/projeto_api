from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario
from comentarios.api.viewsets import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado')