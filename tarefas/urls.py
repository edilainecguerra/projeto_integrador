from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.nova_tarefa, name='nova_tarefa'), 
    path('concluir/<int:id>/', views.concluir_tarefa, name='concluir_tarefa'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

