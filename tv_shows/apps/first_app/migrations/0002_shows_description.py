# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-18 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='description',
            field=models.TextField(default='This movie is cool'),
            preserve_default=False,
        ),
    ]
