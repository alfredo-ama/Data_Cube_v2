# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0015_auto_20160705_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='complete',
            field=models.BooleanField(),
        ),
    ]
