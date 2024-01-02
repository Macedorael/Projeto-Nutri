# Generated by Django 4.1.5 on 2023-11-03 22:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0005_circuferencias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circuferencias',
            name='coxaprossimaldireita',
        ),
        migrations.RemoveField(
            model_name='circuferencias',
            name='coxaprossimalesquerda',
        ),
        migrations.RemoveField(
            model_name='circuferencias',
            name='ponturrilhadireita',
        ),
        migrations.RemoveField(
            model_name='circuferencias',
            name='ponturrilhaesquerda',
        ),
        migrations.AddField(
            model_name='circuferencias',
            name='coxaproximaldireita',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Coxaproximaldireita'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuferencias',
            name='coxaproximalesquerda',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=15, verbose_name='Coxaproximalesquerda'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuferencias',
            name='panturrilhadireita',
            field=models.DecimalField(decimal_places=2, default=2 , max_digits=15, verbose_name='Panturrilhadireita'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuferencias',
            name='panturrilhaesquerda',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15, verbose_name='Panturrilhaesquerda'),
            preserve_default=False,
        ),
    ]
