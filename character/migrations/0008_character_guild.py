# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0007_remove_character_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='guild',
            field=models.CharField(choices=[('fighters', 'FIGHTERS'), ('mages', 'MAGES'), ('undaunted', 'UNDAUNTED'), ('thieves', 'THIEVES'), ('dark brotherhood', 'DARK BROTHERHOOD')], default='fighters', max_length=20),
        ),
    ]
