#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- widgets.models.widget
~~~~~~~~~~~~~~

- This file contains the Widget service models that will map into DB tables and will store Widget data
  and Schema of Widget-Process relations, Rest Client
 """

# future
from __future__ import unicode_literals

# 3rd party
import uuid

# Django
from django.conf import settings
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

# local
from asap.core.models import Authorable, Timestampable

User = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Widget(Authorable, Timestampable, models.Model):
    """Widgets are the collection of different Process & Rules.
       Process can be called based on some rules.Widget consists of a predefined Workflow.

    """

    # Attributes
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text=_('A unique identifier for each Widget. '
                    'Non-editable, to be generated by system itself.'),
    )

    # Functions
    def __str__(self):
        return '{0}'.format(self.uuid)


@admin.register(Widget)
class WidgetAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']
