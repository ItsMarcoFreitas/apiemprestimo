from rest_framework import serializers
from .models import Imovel, Financiamento

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class FinanciamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financiamento
        fields = '__all__'
