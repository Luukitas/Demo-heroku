from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from demo.views import *
from demo.usuario import *

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastrar', cadastrar),
    path('usuario/<int:id>', usuario),
    path('experiencia/<int:id>', experiencia),
    path('cad-empresa', cadastra_empresa),
    path('list-empresa/<int:id>', procura_empresa),
    path('empresa/<int:id>/<str:name>', pagina_empr),
    path('conteudo/<int:id>', conteudo)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)