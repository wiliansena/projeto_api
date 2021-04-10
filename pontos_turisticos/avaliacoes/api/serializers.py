from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao
from avaliacoes.api.viewsets import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'comentario', 'nota', 'data')