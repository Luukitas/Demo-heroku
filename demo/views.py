from django.shortcuts import render, redirect
from demo.models import Pessoa, Empresa, Exp_pessoa
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')   
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})

def login(request):
    contexto = {}
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        usuario = Pessoa.objects.filter(email=email_form).first()
        
    
        if usuario is None:
            print('deu ruim usuario')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        elif usuario.senha is None:
            print('deu ruim senha')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        elif senha_form != usuario.senha:
            print('deu errado')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        else:
            contexto = {
                'pessoa': usuario,
                # 'exp': exp,
            }
            return render(request, 'usuario.html', contexto)

    return render(request, 'login.html', {})

def usuario(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'usuario.html', contexto)

def cadastra_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')   
    else:
        form = EmpresaForm()

    return render(request, 'cad-empresa.html', {'form': form})

def sobre_nos(request):
    return render(request, 'home.html', {})