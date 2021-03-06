# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-20 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='company',
            name='career_page',
            field=models.URLField(blank=True, verbose_name='career page'),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default='Vancouver, BC', max_length=500, verbose_name='location'),
        ),
    ]
