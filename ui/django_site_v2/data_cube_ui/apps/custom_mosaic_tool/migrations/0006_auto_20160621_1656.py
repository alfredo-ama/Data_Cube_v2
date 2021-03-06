# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0005_auto_20160620_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='upper_lat',
            new_name='latitude_max',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='lower_lat',
            new_name='latitude_min',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='upper_long',
            new_name='longitude_max',
        ),
        migrations.RenameField(
            model_name='query',
            old_name='lower_long',
            new_name='longitude_min',
        ),
    ]
