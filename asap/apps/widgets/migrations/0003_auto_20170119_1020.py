# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0002_auto_20170119_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widget',
            name='code',
        ),
        migrations.AddField(
            model_name='widget',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, help_text='Widget token, widget is accessed via this token', verbose_name='Widget token'),
        ),
    ]
