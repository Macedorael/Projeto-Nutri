# Generated by Django 4.2.3 on 2024-01-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plano", "0006_remove_circuferencias_coxaprossimaldireita_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paciente",
            name="sexo",
            field=models.CharField(
                default="masculino", max_length=100, verbose_name="Sexo"
            ),
            preserve_default=False,
        ),
    ]
