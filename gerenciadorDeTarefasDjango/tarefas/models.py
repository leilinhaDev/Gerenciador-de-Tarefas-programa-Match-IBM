from django.db import models

class Tarefa(models.Model):
    descricao = models.CharField(max_length = 255, null = False)
    dataVencimento = models.DateField(null = False)
    prioridadeEscolhas = (
        (1, 'Baixa'),
        (2, 'Media'),
        (3, 'Alta')
    )
    prioridade  = models.IntegerField(null = False, default = 2, choices = prioridadeEscolhas)
    finalizada = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f"{self.descricao}"
