# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0011_delete_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False, verbose_name='产品id')),
                ('name', models.CharField(max_length=100, verbose_name='产品名字')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='产品编号')),
                ('model', models.CharField(max_length=50, unique=True, verbose_name='产品型号')),
                ('classify', models.CharField(max_length=50, verbose_name='产品分类')),
                ('attribute', models.CharField(max_length=50, verbose_name='产品属性')),
                ('valuationMethod', models.CharField(max_length=50, verbose_name='计价方式')),
                ('checking', models.TextField(blank=True, verbose_name='质检方案')),
                ('baiscUnit', models.CharField(blank=True, max_length=20, verbose_name='基本单位')),
                ('inclusionUnit', models.CharField(blank=True, max_length=20, verbose_name='包含单位')),
                ('invoiceType', models.CharField(max_length=20, verbose_name='可开具发票类型')),
                ('tax', models.BooleanField(verbose_name='是否含税')),
                ('inventoryCeiling', models.IntegerField(default=0, verbose_name='库存上限')),
                ('lowerInventoryLimit', models.IntegerField(default=0, verbose_name='库存下限')),
                ('curingCycle', models.CharField(blank=True, max_length=10, verbose_name='养护周期')),
                ('failureLeadTime', models.CharField(blank=True, max_length=10, verbose_name='失效提前期')),
                ('mainSupplier', models.CharField(blank=True, max_length=40, verbose_name='主供应商')),
                ('lpercentage', models.FloatField(default=0, verbose_name='提成比例 （%）')),
                ('explain', models.TextField(blank=True, verbose_name='产品说明')),
                ('parameter', models.TextField(blank=True, verbose_name='产品参数')),
                ('appendix', models.CharField(blank=True, max_length=50, verbose_name='图片附件')),
                ('brand', models.CharField(max_length=20, verbose_name='品牌')),
                ('standard', models.TextField(verbose_name='规格')),
                ('usdOffer', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='USD报价')),
                ('mpq', models.IntegerField(blank=True, default=0, verbose_name='MPQ')),
                ('unit', models.CharField(blank=True, max_length=10, verbose_name='单位')),
                ('ratio', models.FloatField(default=0, verbose_name='比例')),
                ('department', models.CharField(blank=True, max_length=20, verbose_name='部门')),
                ('barCode', models.CharField(blank=True, max_length=50, verbose_name='条形码')),
                ('adviseBid', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='建议进价')),
                ('topBid', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='最高进价')),
                ('adviseSprice', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='建议售价')),
                ('lowerSprice', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='最低售价')),
                ('index', models.IntegerField(default=0, verbose_name='搜索查看数')),
            ],
            options={
                'verbose_name': '物料库',
                'verbose_name_plural': '物料库',
                'ordering': ['index', 'id'],
            },
        ),
    ]
