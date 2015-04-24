# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    fixture = 'initial_data'
    call_command('loaddata', 'initial_data', app_label='grafana')


class Migration(migrations.Migration):

    dependencies = [
        ('grafana', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]
