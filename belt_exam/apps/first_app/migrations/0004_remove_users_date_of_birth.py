# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-22 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20190322_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date_of_birth',
        ),
    ]
