from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    PRIORIDADES = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    prazo = models.DateField()
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
