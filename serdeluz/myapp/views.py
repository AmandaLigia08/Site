from django.shortcuts import render
from .models import Conselho, Projeto

# Listar conselheiros
def list_Conselho(request):
    conselheiros = Conselho.objects.all() #filter(is_ativo=True)
    context = {'conselheiros': conselheiros}
    return render(request, 'list/list-conselho.html', context)

# Create your views here.
def site(request):
    projetos = Projeto.objects.filter(is_principal=True)
    context = {'projetos': projetos}
    return render(request, 'index.html', context)

def sobre(request):
    conselheiros = Conselho.objects.filter(is_ativo=False)
    context = {'conselheiros': conselheiros}
    return render(request, 'sobre.html', context)

def projeto(request, id):
    projetos = Projeto.objects.filter(id=id)
    context = {'projetos': projetos}
    return render(request, 'projeto.html', context)

def contato(request):
    return render(request, 'contato.html')

def chave(request):
    return render(request, 'chave.html')


