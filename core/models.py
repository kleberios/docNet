from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    senha = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Ativo(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    #nome = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fabricante = models.CharField(max_length=30, null=True, blank=True)
    descricao = models.CharField(max_length=50, null=True, blank=True)
    mac = models.CharField(max_length=10)
    ip = models.CharField(max_length=12)
    usuario = models.CharField(max_length=10)
    senha = models.CharField(max_length=10)
    local = models.CharField(max_length=20)
    atualizacao = models.DateField(null=True, blank=True)
    outros = models.TextField(max_length=100)

    def __str__(self):
        return self.tipo.nome


class Server(models.Model):
    nome = models.CharField(max_length=8)
    ip = models.CharField(max_length=14)
    usuario = models.CharField(max_length=15)
    senha = models.CharField(max_length=10)
    descricao = models.TextField(max_length=100)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    nome = models.CharField(max_length=50)
    obs = models.TextField(max_length=100)
