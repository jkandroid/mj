# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-09 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0029_auto_20180809_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='emailLink',
            field=models.CharField(max_length=100, verbose_name='邮箱系统'),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='longitudeLatitude',
            field=models.CharField(max_length=40, verbose_name='公司经纬度'),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='sysLink',
            field=models.CharField(max_length=100, verbose_name='内部系统'),
        ),
    ]