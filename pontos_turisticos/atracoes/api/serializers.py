from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao
from atracoes.api.viewsets import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao','horario_func', 'idade_minima', 'foto')