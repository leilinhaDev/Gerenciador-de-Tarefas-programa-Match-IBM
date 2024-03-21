from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Tarefa
from .forms import TarefaForm


def home(request):
    feitas = Tarefa.objects.filter(finalizada = True)
    naoFeitas = Tarefa.objects.filter(finalizada = False)
    template = loader.get_template('home.html')
    context = {
          'feitas': feitas,
          'naoFeitas': naoFeitas,
    }
    return HttpResponse(template.render(context, request))

def adicionarTarefa(request):
      if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de listagem de tarefas
            return redirect('home')
      else:
        form = TarefaForm()
      return render(request, 'home.html', {'form': form})

def deletarTarefa(request, id):
      tarefa = Tarefa.objects.get(pk=id)
      tarefa.delete()
      return redirect('home')

def mudarTarefa(request, id):
      tarefa = Tarefa.objects.get(pk=id)
      if tarefa.finalizada:
            tarefa.finalizada = False
      else:
            tarefa.finalizada = True
      tarefa.save()
      return redirect('home') 