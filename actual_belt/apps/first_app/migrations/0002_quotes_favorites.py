# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-22 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to='first_app.Users'),
        ),
    ]