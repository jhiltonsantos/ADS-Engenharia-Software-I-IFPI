from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
import random  
import csv, codecs

def home(request):
	tarefas = Tarefa.objects.all()
	return render(request, 'home.html', {'list_tarefa': tarefas})


def importar(request):
	file = request.FILES['arquivo'].read().decode('iso-8859-1')
	alunos = file.replace("\r","").split("\n")
	for aluno in alunos:
		if len(aluno) > 0:
			Aluno.objects.create(nome_aluno = aluno)
	return redirect('home')


def listar_alunos(request):
	alunos = Aluno.objects.all()
	return render(request, 'listar_aluno.html', {'list_aluno': alunos})


def listar_tarefa(request, id_tarefa):
	tarefa = Tarefa.objects.filter(id = id_tarefa).all()
	return render(request, 'listar_tarefa.html', {'list_tarefa': tarefa})


def criar_tarefa(request):
	return render(request, 'criar_tarefa.html')


def create_tarefa(request):
	nome = request.POST['nome']
	desc = request.POST['desc']
	data = request.POST['data']
	Tarefa.objects.create(tarefa = nome, descricao = desc, data_entrega = data)
	return redirect('home')


def sortear(request, id_tarefa):
	alunos = list(Aluno.objects.all())
	sorteado = random.choice(alunos)
	Tarefa.objects.filter(id = id_tarefa).update(aluno = sorteado)
	return redirect(reverse('listar_tarefa', kwargs={'id_tarefa':id_tarefa}))


def editar_tarefa(request, id_tarefa):
	tarefa = Tarefa.objects.filter(id = id_tarefa).all()
	return render(request, 'editar_tarefa.html', {'tarefa': tarefa})


def edit_tarefa(request):
	id_tarefa = request.POST['id_tarefa']
	nome = request.POST['nome']
	desc = request.POST['desc']
	data = request.POST['data']
	Tarefa.objects.filter(id = id_tarefa).update(tarefa = nome, descricao = desc, data_entrega = data)
	return redirect('home')


def excluir_tarefa(request, id_tarefa):
	Tarefa.objects.filter(id = id_tarefa).delete()
	return redirect('home')


def listar_grupo(request):
	grupos = Grupo.objects.all()
	return render(request, 'listar_grupo.html', {'list_grupo': grupos})



