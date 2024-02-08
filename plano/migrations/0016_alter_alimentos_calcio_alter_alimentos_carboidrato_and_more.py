# Generated by Django 4.2.3 on 2024-02-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0015_alter_alimentos_energiakcal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentos',
            name='calcio',
            field=models.FloatField(verbose_name='Cálcio'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='carboidrato',
            field=models.FloatField(verbose_name='Carboidrato'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='cinzas',
            field=models.FloatField(verbose_name='Cinzas'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='cobre',
            field=models.FloatField(verbose_name='Cobre'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='colesterol',
            field=models.FloatField(verbose_name='Colesterol'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='energiakj',
            field=models.FloatField(verbose_name='Energia kj'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='ferro',
            field=models.FloatField(verbose_name='Ferro'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='fibraalimentar',
            field=models.FloatField(verbose_name='Fibra Alimentar'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='fosforo',
            field=models.FloatField(verbose_name='Fósforo '),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='lipideos',
            field=models.FloatField(verbose_name='Lipídeos'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='magnesio',
            field=models.FloatField(verbose_name='Magnésio'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='manganes',
            field=models.FloatField(verbose_name='Manganês'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='niacina',
            field=models.FloatField(verbose_name='Niacina'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='piridoxina',
            field=models.FloatField(verbose_name='Piridoxina'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='potassio',
            field=models.FloatField(verbose_name='Potássio'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='proteina',
            field=models.FloatField(verbose_name='Proteína'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='retinol',
            field=models.FloatField(verbose_name='Retinol'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='riboflavina',
            field=models.FloatField(verbose_name='Riboflavina'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='sodio',
            field=models.FloatField(verbose_name='Sódio'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='tiamina',
            field=models.FloatField(verbose_name='Tiamina'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='vitaminac',
            field=models.FloatField(verbose_name='Vitamina C'),
        ),
        migrations.AlterField(
            model_name='alimentos',
            name='zinco',
            field=models.FloatField(verbose_name='Zinco'),
        ),
    ]