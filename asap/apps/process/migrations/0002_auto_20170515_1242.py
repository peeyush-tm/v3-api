# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 12:42
from __future__ import unicode_literals

import asap.apps.process.schema.validator
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='is_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='process',
            name='schema',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, validators=[asap.apps.process.schema.validator.SchemaValidator()], verbose_name='schema'),
        ),
    ]
