# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('grafana', '0003_auto_20150413_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardDefaultTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256, db_index=True)),
                ('data', jsonfield.fields.JSONField()),
            ],
            options={
                'verbose_name': 'Dashboard template',
                'verbose_name_plural': 'Dashboard templates',
            },
            bases=(models.Model,),
        ),
    ]
