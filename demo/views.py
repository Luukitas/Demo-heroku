from django.shortcuts import render, redirect
from demo.models import Pessoa, Empresa, Exp_pessoa

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
        usuario.dt_nasc = request.POST.get('dt_nasc')
        usuario.save()
        contexto = {
            'msg': 'Salvo com sucesso'
        }
        print('Deu certo')
        return redirect('/')

    return render(request, 'cadastro.html', contexto)

def experiencia(request, id):
    contexto = {
        'id': id
    }
    print('aq')
    if request.method == 'POST':
        pessoa = Pessoa()
        user = Pessoa.objects.filter(id=id).first()
        nome = user.nome
        exp = Exp_pessoa()
        exp.experiencia = user
        exp.valores = request.POST.get('exp')
        exp.save()
        print('ve se foi')
        contexto = {
            'id': id,
            'msg': 'Salvo com sucesso'
        }
        valor = '/experiencia/' + str(id)
        return redirect(valor)
    return render(request, 'experiencia.html', contexto)

def login(request):
    contexto = {}
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        usuario = Pessoa.objects.filter(email=email_form).first()
        # exp = Exp_pessoa.objects.filter(experiencia__exact=usuario.email).all()
        senha = usuario.senha
        print('foi aqui')
        
        
        # for each in usuario.experiencia:

    
        if usuario is None:
            print('deu ruim')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        elif senha_form != senha:
            print('deu errado')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        else:
            contexto = {
                'pessoa': usuario,
                # 'exp': exp,
            }
            valor = '/usuario/' + str(usuario.id)
            return redirect(valor) 

    return render(request, 'login.html', {})

def usuario(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'usuario.html', contexto)

def conteudo(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'conteudo.html', contexto)

def cadastra_empresa(request):
    contexto = {}
    if request.method == 'POST':
        empresa = Empresa()
        empresa.nome = request.POST.get('nome')
        empresa.senha = request.POST.get('senha')
        empresa.linguagens = request.POST.get('linguagens')
        empresa.save()
        print('eeba')
        contexto = {'msg': 'salvo com sucesso'}
        return redirect('/')
    
    return render(request, 'cad-empresa.html', contexto)

def procura_empresa(request):
    contexto = {}
    if request.method == 'POST':
        empresa_form = request.POST.get('empresa')
        empresas = Empresa.objects.filter(nome__icontains=empresa_form).all()

        if empresa_form == "":
            contexto = {'msg': 'Digite algo'}
            return render(request, 'lista-empresa.html', contexto)
        elif empresas is None:
            contexto = {'msg': 'Empresa não encontrada'}
            return render(request, 'lista-empresa.html', contexto)
        else:
            contexto = {
                'empresas': empresas
            }
            return render(request, 'lista-empresa.html', contexto)

    return render(request, 'lista-empresa.html', contexto)

def pagina_empr(request, id):
    empresa = Empresa.objects.filter(id=id).first()
    contexto = {}
    if empresa is not None:
        contexto = {
            'empresa' : empresa
        }
        return render(request, 'empresa.html', contexto)
    return render(request, 'empresa.html', contexto)
    