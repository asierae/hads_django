# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(default='General', max_length=100),
            preserve_default=False,
        ),
    ]
