# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0019_companyinfo_enquiryinfo_goods'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enquiryinfo',
            options={'ordering': ['-isConduct', '-dateTime'], 'verbose_name': '询价申请', 'verbose_name_plural': '询价申请'},
        ),
    ]
