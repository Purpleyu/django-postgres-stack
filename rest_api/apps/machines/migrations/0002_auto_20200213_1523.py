# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-13 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='machine_secret',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='machine secret'),
        ),
    ]
