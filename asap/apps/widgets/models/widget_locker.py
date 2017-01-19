#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- widgets.models.widget_locker
~~~~~~~~~~~~~~

- Widget Locker provides an interface to manage multiple widgets
corresponding to a single identifier.

- The identifier will exchanged with the Veris Runtime service that
may allow multiple runtimes to access the same set of widgets.

- Each Widget however should be able identify the `Entity` accessing itself.

- We need to implement a functionality like [Referer] Header of HTTP Protocol.

[Referer]: https://www.w3.org/Protocols/HTTP/HTRQ_Headers.html#z14

"""

# 3rd party
import uuid

# Django
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

# local
from asap.core.models import Authorable, Timestampable


class WidgetLocker(Authorable, Timestampable, models.Model):
    """Widget Locker model, collection of widgets which will be called based on some rules.
        Every Locker will have a token which will be shared with VRT.

    """

    # Attributes
    name = models.CharField(
            _('Locker Name'),
            max_length=30,
            help_text=_('Required. 30 characters or fewer.'),
    )
    rules = JSONField(
             _('Widget rules'),
             help_text=_('Rules config, tells us which widget will be called based on what rules.'),
    )
    token = models.UUIDField(
        _('Locker token'),
        null=True,
        blank=True,
        unique=True,
        editable=False,
        help_text=_('Non-editable, to be generated by system itself and only when is_publish=True ,\
                    means when Widget Locker is Published.'),
    )
    is_publish = models.BooleanField(
                    _('Publish Locker'),
                    default=False,
                    help_text=_('Only Publish When you are sure. Once published Locker cannot be updated.')
    )

    # Meta
    class Meta:
        verbose_name = _("Widgets Locker")
        verbose_name_plural = _("Widget Locker")
        ordering = ["-created_at"]

    # Functions
    def __str__(self):
        return "Widget Locker {0}".format(self.name)

    def save(self, *args, **kwargs):
        """Override save() method to check if Locker is published if yes, then generate token for locker

        """
        if self.is_publish is True:
            self.token = str(uuid.uuid4())
        return super(WidgetLocker, self).save(*args, **kwargs)


@admin.register(WidgetLocker)
class WidgetLockerAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']
    list_display = ('name', 'token', 'is_publish', )
    list_display_links = ('name', 'token', )
