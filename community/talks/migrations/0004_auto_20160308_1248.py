# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-08 01:48
from __future__ import unicode_literals

from django.db import migrations


def create_events(apps, schema_editor):
    Talk = apps.get_model('talks', 'Talk')
    Event = apps.get_model('events', 'Event')

    for talk in Talk.objects.filter(event=None, presented_on__isnull=False):
        event, __ = Event.objects.get_or_create(
            name='Event on {:%Y-%m-%d}'.format(talk.presented_on),
            date=talk.presented_on)
        talk.event = event
        talk.save()


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0003_talk_event'),
    ]

    operations = [
        migrations.RunPython(create_events, migrations.RunPython.noop),
    ]