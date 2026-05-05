from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tarefa

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'lista.html', {'tarefas': tarefas})

@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        prazo = request.POST.get('prazo')

        Tarefa.objects.create(
            usuario=request.user,
            titulo=titulo,
            prazo=prazo,
            prioridade='M'
        )

        return redirect('/')

    return render(request, 'nova.html')

@login_required
def concluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('/')

@login_required
def excluir_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('/')

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    
    return render(request, 'login.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/login/')


