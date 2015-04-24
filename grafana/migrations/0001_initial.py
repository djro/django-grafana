# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings
import django_grafana.grafana.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
                ('version', models.IntegerField()),
                ('data', jsonfield.fields.JSONField()),
            ],
            options={
                'verbose_name': 'Dashboard',
                'verbose_name_plural': 'Dashboards',
            },
            bases=(django_grafana.grafana.models.ChangedModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('version', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
            bases=(django_grafana.grafana.models.ChangedModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UserInOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.ForeignKey(to='grafana.Organization')),
            ],
            options={
                'verbose_name': 'UserInOrganization',
                'verbose_name_plural': 'UsersInOrganizations',
            },
            bases=(django_grafana.grafana.models.ChangedModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('info', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'UserRole',
                'verbose_name_plural': 'UserRoles',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userinorganization',
            name='role',
            field=models.ForeignKey(to='grafana.UserRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userinorganization',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='grafana.UserInOrganization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='organization',
            field=models.ForeignKey(to='grafana.Organization'),
            preserve_default=True,
        ),
    ]
