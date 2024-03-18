from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tarefa
from datetime import datetime


def home(request):
   # tarefa1 = Tarefa(descricao = 'lavar prato', dataVencimento = datetime.now().date())
   # tarefa2 = Tarefa(descricao = 'tarefa feita', dataVencimento = datetime.now().date(), finalizada = True)
   # tarefa1.save()
   # tarefa2.save()
   
    feitas = Tarefa.objects.filter(finalizada = True)
    naoFeitas = Tarefa.objects.filter(finalizada = False)
 
    template = loader.get_template('home.html')
    context = {
          'feitas': feitas,
          'naoFeitas': naoFeitas,
    }
    

    return HttpResponse(template.render(context, request))

   
