# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-12 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]
