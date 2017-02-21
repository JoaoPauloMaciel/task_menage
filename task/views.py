
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

class Tarefa(object):

    def __init__(self,titulo,data):
        self.titulo=titulo
        self.data=data

    def __str__(self):
        return self.titulo

    ###############################
    def home(request):
        return HttpResponse("Ola")

    def sobre(request):
        return HttpResponse("João Paulo")

    def tarefa(request,valor):
        return HttpResponse("Tarefa: " + str(valor))

    def tarefa(request,ano,mes):
        return HttpResponse("Data: " + str(ano) +"/"+ str(mes))
