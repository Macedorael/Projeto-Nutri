# Generated by Django 4.1.5 on 2023-11-03 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0004_alter_paciente_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circuferencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pescoco', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Pescoço')),
                ('ombro', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ombro')),
                ('torax', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Torax')),
                ('bracodireito', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Braçodireito')),
                ('bracoesquerdo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Braçoesquerdo')),
                ('bracodireitocontraido', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Braçodireitocontraido')),
                ('bracoesquerdocontraido', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Braçoesquerdocontraido')),
                ('antebracodireito', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Antebraçodireito')),
                ('antebracoesquerdo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Antebraçoesquerdo')),
                ('cintura', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Cintura')),
                ('abdome', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Abdome')),
                ('quadril', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Quadril')),
                ('coxadistaldireita', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Coxadistaldireita')),
                ('coxadistalesquerda', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Coxadistalesquerda ')),
                ('coxamedialdireita', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Coxamedialdireita')),
                ('coxamedialesquerda', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Coxamedialesquerda')),
                ('coxaprossimaldireita', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Coxadistaldireita')),
                ('coxaprossimalesquerda', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Coxaprossimalesquerda')),
                ('ponturrilhadireita', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ponturrilhadireita')),
                ('ponturrilhaesquerda', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ponturrilhaesquerda')),
                ('classificacao', models.CharField(max_length=20, verbose_name='Classificação')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.paciente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
