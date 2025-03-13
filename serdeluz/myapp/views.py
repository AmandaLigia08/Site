from django.shortcuts import render
from .models import Conselho, Projeto, Carrocel

# Listar conselheiros
def list_Conselho(request):
    conselheiros = Conselho.objects.all() #filter(is_ativo=True)
    context = {'conselheiros': conselheiros}
    return render(request, 'list/list-conselho.html', context)

# Listar conselheiros
def list_Paralax(request):
    carroceis = Carrocel.objects.all() #filter(is_ativo=True)
    context = {'carroceis': carroceis}
    return render(request, 'navbar.html', context)

# Create your views here.
def site(request):
    projetos = Projeto.objects.filter(is_ativo=False)
    context = {'projetos': projetos}
    return render(request, 'index.html', context)

def sobre(request):
    conselheiros = Conselho.objects.filter(is_ativo=False)
    context = {'conselheiros': conselheiros}
    return render(request, 'sobre.html', context)

def projeto(request):
    projetos = Projeto.objects.filter(is_ativo=False)
    context = {'projetos': projetos}
    return render(request, 'projeto.html', context)

def contato(request):
    return render(request, 'contato.html')

def chave(request):
    return render(request, 'chave.html')

def portal(request):
    return render (request, 'portal.html')


from django.shortcuts import render
from .models import Projeto  # Substitua pelo nome correto do seu modelo

def home(request):
    projetos_destaque = Projeto.objects.all()[:3]  # Pega apenas os 3 primeiros projetos
    return render(request, 'seu_template.html', {'projetos': projetos_destaque})


#PORTAL
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django import forms

# Criar um formulário de registro personalizado
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# View para registrar o usuário
def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redireciona para a página inicial
    else:
        form = RegistroForm()
<<<<<<< HEAD
    return render(request, "registro.html", {"form": form})

=======
    return render(request, "registro.html", {"form": form})
>>>>>>> parent of 3504ff4 (carrosel)
