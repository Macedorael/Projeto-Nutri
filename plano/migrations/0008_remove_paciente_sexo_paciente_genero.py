# Generated by Django 4.2.3 on 2024-01-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plano", "0007_paciente_sexo"),
    ]

    operations = [
        migrations.RemoveField(model_name="paciente", name="sexo",),
        migrations.AddField(
            model_name="paciente",
            name="genero",
            field=models.CharField(
                default="masculino", max_length=100, verbose_name="Genero"
            ),
            preserve_default=False,
        ),
    ]