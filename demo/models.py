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

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.email

