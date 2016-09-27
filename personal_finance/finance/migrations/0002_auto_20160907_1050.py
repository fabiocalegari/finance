# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-07 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('data_resgate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoInvestimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60)),
                ('liquidez_diaria', models.BooleanField(verbose_name=False)),
                ('imposto_de_renda', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='investimento',
            name='tipo_investimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.TipoInvestimento'),
        ),
    ]
