# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-07 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20160907_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investimento',
            name='data_resgate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
