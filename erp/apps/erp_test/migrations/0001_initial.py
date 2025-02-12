# Generated by Django 3.1.12 on 2025-02-12 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='分类名称')),
                ('remark', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32, verbose_name='产品编号')),
                ('name', models.CharField(max_length=64, verbose_name='产品名称')),
                ('barcode', models.CharField(blank=True, max_length=32, null=True, verbose_name='条码')),
                ('spec', models.CharField(blank=True, max_length=64, null=True, verbose_name='规格')),
                ('shelf_life_days', models.IntegerField(null=True, verbose_name='保质期天数')),
                ('purchase_price', models.FloatField(default=0, verbose_name='采购价')),
                ('retail_price', models.FloatField(default=0, verbose_name='零售价')),
                ('remark', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods_set', to='erp_test.goodscategory', verbose_name='产品分类')),
            ],
        ),
    ]
