# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0011_metadata_scene_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='scene_list',
            field=models.CharField(max_length=10000),
        ),
    ]
