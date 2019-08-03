from django.shortcuts import render, redirect
from demo.models import Pessoa

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    contexto = {}
    if(request.method == 'POST'):
        usuario = Pessoa()
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.senha = request.POST.get('senha')
        usuario.save()
        contexto = {
            'msg': 'Salvo com sucesso'
        }
        print('Deu certo')
        return redirect('/')

    return render(request, 'cadastro.html', contexto)

def login(request):
    contexto = {}
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        usuario = Pessoa.objects.filter(email=email_form).first()
        senha = usuario.senha
        
        if usuario is None:
            print('deu ruim')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        elif senha_form != senha:
            print('deu errado')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        else:
            print("Deu certo")
            contexto = {
                'pessoa': usuario
            }
            return render(request, 'usuario.html', contexto) 
        return contexto['pessoa']

    return render(request, 'login.html', {})