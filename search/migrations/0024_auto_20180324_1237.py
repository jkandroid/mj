# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0023_auto_20180317_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='./upload/goods', verbose_name='图片'),
        ),
    ]