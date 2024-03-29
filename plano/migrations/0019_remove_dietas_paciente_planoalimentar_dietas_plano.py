# Generated by Django 4.2.3 on 2024-02-20 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0018_alter_dietas_quantidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dietas',
            name='paciente',
        ),
        migrations.CreateModel(
            name='PlanoAlimentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=30, verbose_name='Plano')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.paciente')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dietas',
            name='plano',
            field=models.ForeignKey(default=None,null=True, on_delete=django.db.models.deletion.CASCADE, to='plano.planoalimentar'),
            preserve_default=False,
        ),
    ]
