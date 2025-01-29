from django.shortcuts import render

# Create your views here.
def site(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def projeto(request):
    return render(request, 'projeto.html')

def contato(request):
    return render(request, 'contato.html')