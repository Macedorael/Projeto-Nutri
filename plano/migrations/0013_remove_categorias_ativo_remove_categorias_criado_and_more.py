# Generated by Django 4.2.3 on 2024-02-07 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0012_remove_alimentos_monoinsaturados_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorias',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='categorias',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='categorias',
            name='modificado',
        ),
    ]