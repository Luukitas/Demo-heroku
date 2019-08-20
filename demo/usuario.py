from django.shortcuts import render, redirect, get_object_or_404
from demo.models import Pessoa, Empresa, Exp_pessoa
from demo import views
from .forms import *
from django.db import connection

def conteudo(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'conteudo.html', contexto)

def experiencia(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        form.valores = request.POST.get('valores')
        print(id)
        if form.is_valid:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Exp_pessoa(experiencia, valores) VALUES (id, %s)', [id, form.valores])
            return redirect('/experiencia/' + str(id))
        
    else:
        form = ExperienciaForm()

    return render(request, 'experiencia.html', { 'pessoa': pessoa, 'form': form})


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
    pessoa = Pessoa.objects.filter(id=id)
    usuario = get_object_or_404(Pessoa, pk=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid:
            print('foi')
            form.save()
            return redirect('/')

    else:
        print('AQ')
        form = UsuarioForm()
    
    return render(request, 'configuracoes.html', {'pessoa': pessoa, 'form': form})
    
    
