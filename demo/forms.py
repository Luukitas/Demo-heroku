from django import forms
from proj import settings
from .models import *

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'senha', 'profissao', 'img_perfil']

class EmpresaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Empresa
        fields = ['nome', 'senha', 'cpf', 'estado', 'cidade', 'rua', 'numero', 'complemento', 'atuacao', 'img_perfil', 'descricao', 'linguagens']

class ExperienciaForm(forms.ModelForm):

    class Meta:
        model = Exp_pessoa
        fields = ['valores']
        