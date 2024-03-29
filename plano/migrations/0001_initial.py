# Generated by Django 4.1.5 on 2023-11-02 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('peso', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Peso')),
                ('proteina', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Proteina')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('refeicoes', models.CharField(max_length=30, verbose_name='Refeições')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Peso')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Altura')),
                ('imc', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Imc')),
                ('classificacao', models.CharField(max_length=20, verbose_name='Classificação')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.paciente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dietas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.alimento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.paciente')),
                ('refeicoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.refeicao')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
