# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 07:56
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='widgetlocker',
            options={'ordering': ['-created_at'], 'verbose_name': 'Widgets Locker', 'verbose_name_plural': 'Widget Locker'},
        ),
        migrations.RemoveField(
            model_name='widget',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='widgetlocker',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='widgetlocker',
            name='widgets',
        ),
        migrations.AddField(
            model_name='widget',
            name='code',
            field=models.CharField(default=1, help_text='Required & Unique. 30 characters or fewer.', max_length=30, unique=True, verbose_name='Widget code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widget',
            name='name',
            field=models.CharField(default=1, help_text='Required. 30 characters or fewer.', max_length=30, verbose_name='Widget Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widget',
            name='process_locker_token',
            field=models.UUIDField(default=uuid.uuid4, help_text='Token of Process Locker to which will be loaded when a Widget is called.', verbose_name='Process Locker Token'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widget',
            name='schema',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Rules config, tells us which widget will be called based on what rules.', verbose_name='Widget Schema'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widgetlocker',
            name='is_publish',
            field=models.BooleanField(default=False, help_text='Only Publish When you are sure. Once published Locker cannot be updated.', verbose_name='Publish Locker'),
        ),
        migrations.AddField(
            model_name='widgetlocker',
            name='name',
            field=models.CharField(default=1, help_text='Required. 30 characters or fewer.', max_length=30, verbose_name='Locker Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widgetlocker',
            name='rules',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, help_text='Rules config, tells us which widget will be called based on what rules.', verbose_name='Widget rules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='widgetlocker',
            name='token',
            field=models.UUIDField(blank=True, editable=False, help_text='Non-editable, to be generated by system itself and only when is_publish=True ,                    means when Widget Locker is Published.', null=True, unique=True, verbose_name='Locker token'),
        ),
    ]
