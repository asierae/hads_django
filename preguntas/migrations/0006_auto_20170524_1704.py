# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_auto_20170522_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(blank=True, to='preguntas.Choice'),
        ),
    ]
