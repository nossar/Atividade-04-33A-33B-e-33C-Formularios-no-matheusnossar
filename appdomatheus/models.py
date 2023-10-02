from django.db import models


class MusicosFavoritos(models.Model):
    nome = models.CharField(max_length=50)
    data_de_nascimento = models.DateField()
    banda = models.CharField(max_length=20)
    instrumento = models.CharField(max_length=20)


class BandasFavoritas(models.Model):
    ESTILO = [
        ("A", "Alegre"),
        ("P", "Pesado"),
        ("T", "Triste"),
    ]
    nome = models.CharField(max_length=30)
    ano_de_inicio = models.IntegerField()
    popularidade = models.IntegerField()
    estilo = models.CharField(max_length=1, choices=ESTILO)
