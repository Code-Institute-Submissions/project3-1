# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_auto_20180405_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='image',
        ),
    ]
