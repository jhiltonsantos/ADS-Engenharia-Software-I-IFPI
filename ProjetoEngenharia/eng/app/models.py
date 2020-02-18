from django.conf import settings
from django.db import models
from django.utils import timezone


class GrupoTarefa(models.Model):
    grupo = models.CharField('Grupo', max_length=100)


class Aluno(models.Model):
    nome_aluno = models.CharField('Nome', max_length=100)
    grupo = models.ForeignKey(GrupoTarefa, on_delete=models.CASCADE, null=True)


class Evento(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descricao', blank=True)
    data_inicial = models.DateTimeField('DataInicial', null=True)
    data_final = models.DateTimeField('DataFinal', null=True)
    datasApresentacao = models.CharField('Datas', max_length=200, null=True)


class Tarefa(models.Model):
    tarefa = models.CharField('Tarefa', max_length=100)
    descricao = models.TextField('Descricao', blank=True)
    duracao = models.IntegerField('Duracao', null=False, default=0)
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.ForeignKey(
        GrupoTarefa, on_delete=models.CASCADE, null=True, blank=True)
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, null=True, blank=True)
