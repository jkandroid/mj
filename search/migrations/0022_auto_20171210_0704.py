# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0021_auto_20171210_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='tax',
            field=models.BooleanField(default=True, verbose_name='是否含税'),
        ),
    ]