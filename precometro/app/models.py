from django.db import models

class Supermercado(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.marca})" if self.marca else self.nome


class Preco(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_alteracao = models.DateTimeField(auto_now_add=True)  # Salva data e hora automaticamente
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.produto.nome} - R$ {self.valor} no {self.supermercado.nome}"