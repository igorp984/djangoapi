from django.db import models

# Create your models here.
class Produto(models.Model):
    name = models.CharField("Nome", max_length=100)
    preco_unitario = models.DecimalField("Preço Unitário", max_digits=10, decimal_places=2)
    multiplo = models.IntegerField("Múltiplo")
