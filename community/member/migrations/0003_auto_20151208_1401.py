# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20151208_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='meetup_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='member.MeetupUser', verbose_name='meetup user'),
        ),
    ]
