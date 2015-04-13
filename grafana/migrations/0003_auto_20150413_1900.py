# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grafana', '0002_auto_20150413_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='info',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
