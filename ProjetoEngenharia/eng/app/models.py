from django.conf import settings
from django.db import models
from django.utils import timezone



class Aluno(models.Model):
	nome_aluno = models.CharField('Nome', max_length=100)


class GrupoTarefa(models.Model):
	grupo = models.CharField('Grupo', max_length=100)


class Grupo_Aluno(models.Model):
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	grupo = models.ForeignKey(GrupoTarefa, on_delete=models.CASCADE)


class Tarefa(models.Model):
	tarefa = models.CharField('Tarefa', max_length=100)
	descricao = models.TextField('Descricao', blank=True)
	data_entrega = models.DateField('Data de entrega', null=True, blank=True)
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True)
	grupo = models.ForeignKey(GrupoTarefa, on_delete=models.CASCADE, null=True, blank=True)
