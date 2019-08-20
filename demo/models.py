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

    profissao = models.CharField(
        max_length=255,
        verbose_name='profissão',
        null=True,
        blank=True,
    )

    img_perfil = models.ImageField(
        upload_to='images_pessoa/',
        verbose_name='Imagem',
        blank=True,
        null=True
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

    ESTADO = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    cidade = models.CharField(
        max_length=255,
        verbose_name='Cidade',
        blank=True,
        null=True
    )

    rua = models.CharField(
        max_length=255,
        verbose_name='Rua',
        blank=True,
        null=True
    )

    numero = models.CharField(
        max_length=255,
        verbose_name='Numero',
        blank=True,
        null=True
    )

    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento',
        blank=True,
        null=True
    )

    img_perfil = models.ImageField(
        upload_to='images/',
        verbose_name='Imagem',
        blank=True,
        null=True
    )

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome',
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='Senha',
    )

    estado = models.CharField(
        verbose_name='Estado',
        choices=ESTADO,
        max_length=255,
        blank=True,
        null=True
    )

    atuacao = models.CharField(
        max_length=255,
        verbose_name='Atuacao',
        blank=True,
        null=True
    )

    cpf = models.CharField(
        max_length=20,
        verbose_name='Cpf',
        blank=True,
        null=True
    )

    descricao = models.TextField(
        verbose_name='Descricao',
        blank=True,
        null=True
    )

    linguagens = models.TextField(
        verbose_name='Linguagens',
        blank=True,
        null=True
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

