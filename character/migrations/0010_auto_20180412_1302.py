# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-12 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0009_auto_20180406_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='classes',
            field=models.CharField(choices=[('dragonknight', 'DRAGONKNIGHT'), ('sorcerer', 'SORCERER'), ('nightblade', 'NIGHTBLADE'), ('templar', 'TEMPLAR'), ('warden', 'WARDEN')], default='dragonknight', max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='m', max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='guild',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('fighters', 'FIGHTERS'), ('mages', 'MAGES'), ('undaunted', 'UNDAUNTED'), ('thieves', 'THIEVES'), ('dark brotherhood', 'DARK BROTHERHOOD')], max_length=49),
        ),
        migrations.AlterField(
            model_name='character',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='tag',
            field=models.CharField(max_length=300, null=True),
        ),
    ]