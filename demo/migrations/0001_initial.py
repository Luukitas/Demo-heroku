# Generated by Django 2.2.4 on 2019-08-08 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('senha', models.CharField(max_length=255, verbose_name='senha')),
                ('linguagens', models.TextField(blank=True, max_length=255, null=True, verbose_name='linguagens')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True, verbose_name='nome')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='e-mail')),
                ('senha', models.CharField(max_length=255, verbose_name='senha')),
                ('dt_nasc', models.DateField(blank=True, null=True, verbose_name='data de nascimento')),
                ('experiencia', models.CharField(blank=True, max_length=255, null=True, verbose_name='experiencia')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exp_pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.Pessoa')),
            ],
        ),
    ]