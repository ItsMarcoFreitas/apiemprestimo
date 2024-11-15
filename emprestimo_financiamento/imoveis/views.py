from rest_framework import viewsets
from .models import Imovel, Financiamento
from .serializers import ImovelSerializer, FinanciamentoSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class FinanciamentoViewSet(viewsets.ModelViewSet):
    queryset = Financiamento.objects.all()
    serializer_class = FinanciamentoSerializer
