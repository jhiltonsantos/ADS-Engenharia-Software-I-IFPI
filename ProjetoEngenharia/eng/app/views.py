from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
import random  
import csv, codecs
from datetime import datetime, date

def home(request):
	tarefas = Tarefa.objects.all()
	return render(request, 'home.html', {'list_tarefa': tarefas})


def ordenacao(request):
	ordem = request.POST['ordem']
	tarefas = list()
	if ordem == '1':
		tarefas = Tarefa.objects.all().order_by('data_entrega')
	elif ordem == '2':
		tarefas = Tarefa.objects.all().order_by('duracao')
	return render(request, 'home.html', {'list_tarefa': tarefas, 'opcao_ordenacao': ordem})


def importar_arquivo(request):
	return render(request, 'importar.html')


def importar(request):
	alunos = Aluno.objects.all()
	if len(alunos) == 0:
		file = request.FILES['file-upload'].read().decode('iso-8859-1')
		alunos = file.replace("\r","").split("\n")
		for aluno in alunos:
			if len(aluno) > 0:
				Aluno.objects.create(nome_aluno = aluno)
	return redirect('listar_alunos')


def listar_alunos(request):
	alunos = Aluno.objects.all()
	return render(request, 'listar_aluno.html', {'list_aluno': alunos})


def listar_tarefa(request, id_tarefa):
	tarefa = Tarefa.objects.filter(id = id_tarefa)
	return render(request, 'listar_tarefa.html', {'list_tarefa': tarefa})


def criar_tarefa(request):
	return render(request, 'criar_tarefa.html')


def create_tarefa(request):
	nome = request.POST['nome']
	desc = request.POST['desc']
	data = request.POST['data']
	duracao = request.POST['duracao']
	Tarefa.objects.create(tarefa = nome, descricao = desc, data_entrega = data, duracao = duracao)
	return redirect('home')


def sortear(request, id_tarefa):
	alunos = list(Aluno.objects.all())
	grupos = list(GrupoTarefa.objects.all())
	list_sorteio = alunos + grupos
	sorteado = random.choice(list_sorteio)
	if type(sorteado) == Aluno:
		Tarefa.objects.filter(id = id_tarefa).update(aluno = sorteado, grupo = None)
	else:
		Tarefa.objects.filter(id = id_tarefa).update(grupo = sorteado, aluno = None)
	return redirect(reverse('home'))


def sorteio(request):
	tarefas = Tarefa.objects.all()
	grupos = GrupoTarefa.objects.all()
	alunos = Aluno.objects.all()
	return render(request, 'sorteio.html', {'list_tarefa': tarefas, 'list_grupo': grupos, 'list_aluno': alunos})


def gerar_sorteio(request):
	tarefas = request.POST.getlist('tarefas[]')
	grupos = request.POST.getlist('grupos[]') 
	if len(grupos) > 0:
		for i in tarefas:
			grupo = random.choice(grupos)
			grupo_sorteado = GrupoTarefa.objects.filter(id = grupo)
			Tarefa.objects.filter(id = i).update(grupo = grupo_sorteado[0], aluno = None)
			grupos.remove(grupo)
	else:
		alunos = list(Aluno.objects.all())
		for i in tarefas:
			aluno_sorteado = random.choice(alunos)
			Tarefa.objects.filter(id = i).update(aluno = aluno_sorteado, grupo = None)
			alunos.remove(aluno_sorteado)
	return redirect('home')


def editar_tarefa(request, id_tarefa):
	tarefa = Tarefa.objects.filter(id = id_tarefa)
	return render(request, 'editar_tarefa.html', {'tarefa': tarefa})


def edit_tarefa(request):
	id_tarefa = request.POST['id_tarefa']
	nome = request.POST['nome']
	desc = request.POST['desc']
	data = request.POST['data']
	duracao = request.POST['duracao']
	Tarefa.objects.filter(id = id_tarefa).update(tarefa = nome, descricao = desc, data_entrega = data, duracao = duracao)
	return redirect('home')


def excluir_tarefa(request, id_tarefa):
	Tarefa.objects.filter(id = id_tarefa).delete()
	return redirect('home')


def criar_grupo(request):
	total_aluno_disp = len(Aluno.objects.filter(grupo = None))
	return render(request, 'criar_grupo.html', { 'aluno_disp': total_aluno_disp })


def create_grupo(request):
	tipo = request.POST['rb-grupos']
	quant = int(request.POST['quant'])
	alunos = list(Aluno.objects.filter(grupo = None))
	grupos = list()
	if tipo == 'aluno':
		quant_grupo = len(alunos) // int(quant)
		if len(alunos) % int(quant) > 1:
			quant_grupo += 1
		for i in range (quant_grupo):
			grupos.append(GrupoTarefa.objects.create())
		for grupo in grupos:
			for i in range (quant):
				recebe_grupo = random.choice(alunos)
				Aluno.objects.filter(id = recebe_grupo.id).update(grupo = grupo)
				alunos.remove(recebe_grupo)
				if len(alunos) == 0:
					break
	else:
		quant_alunos = len(alunos) // int(quant)
		for i in range (quant):
			grupos.append(GrupoTarefa.objects.create())
		for grupo in grupos:
			for i in range (quant_alunos):
				recebe_grupo = random.choice(alunos)
				Aluno.objects.filter(id = recebe_grupo.id).update(grupo = grupo)
				alunos.remove(recebe_grupo)
		if len(alunos) != 0:
			for grupo in grupos:
				recebe_grupo = random.choice(alunos)
				Aluno.objects.filter(id = recebe_grupo.id).update(grupo = grupo)
				alunos.remove(recebe_grupo)
				if len(alunos) == 0:
					break
	return redirect('listar_grupos')


def excluir_grupo(request, id_grupo):
	Aluno.objects.filter(grupo = id_grupo).update(grupo = None)
	Tarefa.objects.filter(grupo = id_grupo).update(grupo = None)
	GrupoTarefa.objects.filter(id = id_grupo).delete()
	return redirect('listar_grupos')


def listar_grupos(request):
	grupos = GrupoTarefa.objects.all()
	alunos = list()
	for i in grupos:
		alunos += Aluno.objects.filter(grupo = i)
	return render(request, 'listar_grupo.html', {'list_grupo': grupos, 'list_aluno': alunos})


def listar_evento(request):
	eventos = Evento.objects.all()
	tarefas = Tarefa.objects.all()
	return render(request, 'listar_evento.html', {'list_evento': eventos, 'list_tarefa_evento': tarefas})


def detalhes_evento(request, id_evento):
	evento = Evento.objects.filter(id = id_evento)
	tarefas = Tarefa.objects.filter(evento = id_evento)
	return render(request, 'detalhes_evento.html', {'list_evento': evento, 'list_tarefa_evento': tarefas})


def criar_evento(request):
	tarefas_disponiveis = Tarefa.objects.all()
	return render(request, 'criar_evento.html', { 'tarefas_disp': tarefas_disponiveis })


def create_evento(request):
	print('ok')
	tarefas = request.POST.getlist('tarefas[]')
	dias = ['Seg','Ter','Qua','Qui','Sex','Sab','Dom']

	titulo = request.POST['nome']
	desc = request.POST['desc']
	diaSelecionado = request.POST.getlist('dias[]')

	dataInicial = request.POST['dtIni']
	dtIni = datetime.strptime(dataInicial, '%Y-%m-%d').date()
	dataFinal = request.POST['dtFim']
	dtFin = datetime.strptime(dataFinal, '%Y-%m-%d').date()
	dtFin = date.fromordinal(dtFin.toordinal()+1)
	data = ''
	while dtIni != dtFin:
		dia_da_semana = dtIni.weekday()
		for i in diaSelecionado:
			if dias[dia_da_semana] == i:
				data += str(dtIni) + '|'
		dtIni = date.fromordinal(dtIni.toordinal()+1)
	Evento.objects.create(titulo = titulo, descricao = desc, data_inicial = dataInicial, data_final = dataFinal, datasApresentacao = data)
	evento = Evento.objects.latest('id')
	for t in tarefas:
		Tarefa.objects.filter(id = t).update(evento = evento.id)
	return redirect('listar_evento')


def excluir_evento(request, id_evento):
	Tarefa.objects.filter(evento = id_evento).update(evento = None)
	Evento.objects.filter(id = id_evento).delete()
	return redirect('listar_evento')

