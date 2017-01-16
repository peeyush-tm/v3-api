# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 06:13
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema', django.contrib.postgres.fields.jsonb.JSONField(help_text='Resource swagger client schema.', verbose_name='Resource schema')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Non-editable, to be generated by system itself.', verbose_name='created at')),
                ('resource', models.ForeignKey(help_text='Resource to which this schema belongs too.', on_delete=django.db.models.deletion.CASCADE, related_name='resource_schema', to='store.Resource', verbose_name='resource')),
            ],
            options={
                'verbose_name': 'Resource Schema',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Resources Schema',
            },
        ),
    ]
