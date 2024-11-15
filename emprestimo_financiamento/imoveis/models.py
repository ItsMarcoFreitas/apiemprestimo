from django.db import models

class Imovel(models.Model):
    endereco = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.endereco

class Financiamento(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='financiamentos')
    valor_financiado = models.DecimalField(max_digits=12, decimal_places=2)
    taxa_juros = models.DecimalField(max_digits=4, decimal_places=2)
    data_inicio = models.DateField()
    prazo_anos = models.IntegerField()

    def __str__(self):
        return f"Financiamento de {self.imovel.endereco}"
