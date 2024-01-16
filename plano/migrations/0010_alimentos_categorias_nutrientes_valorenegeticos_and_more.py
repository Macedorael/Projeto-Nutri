# Generated by Django 4.1.5 on 2024-01-15 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0009_circuferencias_rcq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nutrientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('unidade', models.CharField(max_length=100, verbose_name='Unidade')),
            ],
        ),
        migrations.CreateModel(
            name='Valorenegeticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.alimentos')),
                ('nutriente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.nutrientes')),
            ],
        ),
        migrations.AddField(
            model_name='alimentos',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.categorias'),
        ),
        migrations.AlterField(
            model_name='dietas',
            name='alimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.alimentos'),
        ),
        migrations.DeleteModel(
            name='Alimento',
        ),
    ]
