# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_remove_users_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date_of_birth',
            field=models.DateField(default='2016-04-06'),
            preserve_default=False,
        ),
    ]