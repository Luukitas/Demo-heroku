# Generated by Django 2.2.4 on 2019-08-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exp_pessoa',
            name='valores',
            field=models.TextField(blank=True, null=True, verbose_name='valores'),
        ),
    ]
