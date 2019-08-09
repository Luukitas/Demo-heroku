from django.urls import path, include
from demo.views import index, login, cadastrar, experiencia, cadastra_empresa, procura_empresa, pagina_empr, usuario, conteudo

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastrar', cadastrar),
    path('usuario/<int:id>', usuario),
    path('experiencia/<int:id>', experiencia),
    path('cad-empresa', cadastra_empresa),
    path('list-empresa', procura_empresa),
    path('empresa/<int:id>', pagina_empr),
    path('conteudo/<int:id>', conteudo)
]