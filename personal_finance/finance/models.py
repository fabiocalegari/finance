from django.db import models
from enum import unique

# Create your models here.
class Lancamento (models.Model):
    data_lancamento = models.DateField()
    
class TipoInvestimento (models.Model):
    descricao = models.CharField(max_length = 60)
    liquidez_diaria = models.BooleanField(False)
    imposto_de_renda = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.descricao
    
class Investimento (models.Model):
    tipo_investimento = models.ForeignKey(TipoInvestimento)
    descricao = models.CharField(max_length = 100)
    data_resgate = models.DateField(null = True, blank = True)
    
    def __str__(self):
        return self.descricao

class TipoMovimento (models.Model):
    descricao = models.CharField(max_length = 50)
        
    def __str__(self):
        return self.descricao
        
class Movimento (models.Model):
    investimento = models.ForeignKey(Investimento)
    tipo_movimento = models.ForeignKey(TipoMovimento)
    data_movimento = models.DateField()
    valor_movimento = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.investimento.__str__() + ' => ' + self.tipo_movimento.__str__() + ' de ' + self.valor_movimento.__str__() + ' em ' + self.data_movimento.__str__()