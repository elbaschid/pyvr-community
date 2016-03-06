# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-06 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='presented_on',
            field=models.DateField(blank=True, null=True, verbose_name='presented on'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='summary',
            field=models.TextField(blank=True, verbose_name='summary'),
        ),
    ]