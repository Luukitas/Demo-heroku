from django.db import models

# Create your models here.

class Pessoa(models.Model):

    nome = models.CharField(
        max_length=255,
        verbose_name='nome',
        null=True,
        blank=True,        
    )

    email = models.EmailField(
        max_length=255,
        verbose_name= 'e-mail',
        unique=True,
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='senha'
    )

    dt_nasc = models.DateField(
        verbose_name='data de nascimento',
        null=True,
        blank=True,
    )

    experiencia = models.CharField(
        max_length=255,
        verbose_name='experiencia',
        null=True,
        blank=True,
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Exp_pessoa(models.Model):

    experiencia = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    valores = models.TextField(
        verbose_name='valores',
        null=True,
        blank=True
    )


class Empresa(models.Model):

    nome = models.CharField(
        max_length=255,
        verbose_name='nome',
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='senha',
    )

    linguagens = models.TextField(
        max_length=255,
        verbose_name='linguagens',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome
