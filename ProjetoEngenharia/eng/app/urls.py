from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ordenacao', views.ordenacao, name='ordenacao'),
    path('importar_arquivo/', views.importar_arquivo, name='importar_arquivo'),
    path('importar/', views.importar, name='importar'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
    path('listar_tarefa/<int:id_tarefa>',
         views.listar_tarefa, name='listar_tarefa'),
    path('listar_grupos/', views.listar_grupos, name='listar_grupos'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('create_tarefa/', views.create_tarefa, name='create_tarefa'),
    path('editar_tarefa/<int:id_tarefa>',
         views.editar_tarefa, name='editar_tarefa'),
    path('edit_tarefa/', views.edit_tarefa, name='edit_tarefa'),
    path('excluir_tarefa/<int:id_tarefa>',
         views.excluir_tarefa, name='excluir_tarefa'),
    path('excluir_grupo/<int:id_grupo>',
         views.excluir_grupo, name='excluir_grupo'),
    path('sortear/<int:id_tarefa>', views.sortear, name='sortear'),
    path('sorteio/', views.sorteio, name='sorteio'),
    path('gerar_sorteio/', views.gerar_sorteio, name='gerar_sorteio'),
    path('criar_grupo/', views.criar_grupo, name='criar_grupo'),
    path('create_grupo/', views.create_grupo, name='create_grupo'),
    path('listar_evento/', views.listar_evento, name='listar_evento'),
    path('detalhes_evento/<int:id_evento>',
         views.detalhes_evento, name='detalhes_evento'),
    path('criar_evento/', views.criar_evento, name='criar_evento'),
    path('create_evento/', views.create_evento, name='create_evento'),
    path('excluir_evento/<int:id_evento>',
         views.excluir_evento, name='excluir_evento'),

]
