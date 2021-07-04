from django.db import models


class Contacto(models.Model):
    Nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    Nome = models.CharField(max_length=200)
    comentario = models.CharField(max_length=1000)

