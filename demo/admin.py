from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Pessoa)
admin.site.register(models.Empresa)
admin.site.register(models.Exp_pessoa)