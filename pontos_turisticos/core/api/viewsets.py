from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).delete(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def denunciar(self, request, pk=None):
        pass


    @action(methods=['GET'], detail=True)
    def teste(self, request):
        pass

