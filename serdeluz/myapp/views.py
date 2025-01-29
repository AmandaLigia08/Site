from django.shortcuts import render
from .models import Conselho

# Create your views here.
def site(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def projeto(request):
    return render(request, 'projeto.html')

def contato(request):
    return render(request, 'contato.html')

# Listar conselheiros
def list_Conselho(request):
    conselheiros = Conselho.objects.filter(is_ativo=False)
    context = {'conselheiros ': conselheiros}
    return render(request, 'list/list-conselho.html', context)