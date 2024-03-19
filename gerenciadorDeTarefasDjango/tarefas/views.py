from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tarefa



def home(request):
    feitas = Tarefa.objects.filter(finalizada = True)
    naoFeitas = Tarefa.objects.filter(finalizada = False)
    template = loader.get_template('home.html')
    context = {
          'feitas': feitas,
          'naoFeitas': naoFeitas,
    }
    return HttpResponse(template.render(context, request))

   
