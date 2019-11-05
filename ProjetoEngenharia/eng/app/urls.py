from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('importar/', views.importar, name='importar'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
    path('listar_tarefa/<int:id_tarefa>', views.listar_tarefa, name='listar_tarefa'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('create_tarefa/', views.create_tarefa, name='create_tarefa'),
    path('editar_tarefa/<int:id_tarefa>', views.editar_tarefa, name='editar_tarefa'),
    path('edit_tarefa/', views.edit_tarefa, name='edit_tarefa'),
    path('excluir_tarefa/<int:id_tarefa>', views.excluir_tarefa, name='excluir_tarefa'),
    path('sortear/<int:id_tarefa>', views.sortear, name='sortear'),

]
