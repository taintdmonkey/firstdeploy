# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-05 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20180305_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
