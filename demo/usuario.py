from django.shortcuts import render, redirect
from demo.models import Pessoa, Empresa, Exp_pessoa
from demo import views
from .forms import *

def conteudo(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'conteudo.html', contexto)

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


def procura_empresa(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
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
                'empresas' : empresas
            }
            return render(request, 'lista-empresa.html', {'pessoa': pessoa, 'empresas':empresas})

    return render(request, 'lista-empresa.html', contexto)

def pagina_empr(request, id, name):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    empresa = Empresa.objects.filter(nome=name).first()
    contexto = {}
    if empresa is not None:
        return render(request, 'empresa.html', {'pessoa': pessoa, 'empresa': empresa})    
    return render(request, 'empresa.html', contexto)

def configuracao(request, id):
    pessoa = Pessoa.objects.filter(id=id).filter()
    form = UsuarioForm(request.POST, request.GET)

    # if form.is_valid:

    
    
