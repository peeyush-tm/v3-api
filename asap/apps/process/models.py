#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- process.models
~~~~~~~~~~~~~~

- This file contains the Process service models that will map into DB tables and will store Process data
  and Process-Resource Relation
 """

# future
from __future__ import unicode_literals

# 3rd party
import uuid, bleach

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError

# local
from asap.apps.utils import validator


class Process(models.Model):
    """
    Every Process is connected with a resource and itself it is blind.
          For every action it asks his Resource for instructions.
    """

    # Attributes
    name = models.CharField(
            _('Process Name'),
            max_length=30,
            help_text=_('Required. 30 characters or fewer.'),
    )
    token = models.UUIDField(
        _('Process token'),
        default=uuid.uuid4,
        help_text=_('Process token, process is accessed via this token.'),
    )
    resource_token = models.UUIDField(
                        _('Resource Token'),
                        help_text=_('Token of Resource to which this Process belongs too.')
    )
    operation = models.CharField(
                        _('Resource operation'),
                        max_length=255,
                        help_text=_('Operation of Resource to which this Process will call')
    )
    created_at = models.DateTimeField(
                 _('created at'),
                 auto_now_add=True,
                 db_index=True,
                 editable=False,
                 help_text=_('Non-editable, to be generated by system itself.'),
    )

    # the process will receive a part of the swagger schema
    # process corresponds to a **single operation** of any path of the swagger schema
    # note: only consume parameters from the schema
    # and add more stuff when required,
    # as discussed with @ND, bravado takes care of everything (headers, http method, etc),
    # all we need is data. So only params as of now
    # resource_token is being treated as the endpoint as of now
    endpoint_schema = JSONField(
        _('schema'),
        help_text=_('A part of Schema from the Swagger Client from the resource server'),
    )

    # Meta
    class Meta:
        verbose_name = _("Process")
        verbose_name_plural = _("Processes")
        ordering = ["-created_at"]

    # Functions
    def __str__(self):
        return "Process {0}".format(self.name)

    def clean(self):
        """Validate models field data or clean fields data so that no bad strings can cause any problem.
        """

        # reject any malicious input string
        bad_strings_json = validator._get_bad_strings_json().get('rejected_list')

        if self.name in bad_strings_json:
            raise ValidationError(_('malicious input string sent in name. {0}'.format(self.name)))

        if self.operation in bad_strings_json:
            raise ValidationError(_('malicious input string found in operation. {0}'.format(self.operation)))

        # validate char fields data length
        if len(self.name) > 30:
            raise ValidationError({'name': _('Length of name cannot be greater then 30')})
        if len(self.operation) > 255:
            raise ValidationError({'name': _('Length of name cannot be greater then 255')})

        # clean or bleach fields data
        self.name, self.operation = bleach.clean(self.name), bleach.clean(self.operation)

    def save(self, **kwargs):
        self.clean()
        return super(Process, self).save(**kwargs)


class ProcessLocker(models.Model):
    """
        Process Locker is the collection of Processes which will be called based on some rules.
        Every Locker will have a token which will be shared with Widget.
    """

    # Attributes
    name = models.CharField(
            _('Locker Name'),
            max_length=30,
            help_text=_('Required. 30 characters or fewer.'),
    )
    rules = JSONField(
             _('Process rules'),
             help_text=_('Rules config, tells us which process will be called based on what rules.'),
    )
    token = models.UUIDField(
        _('Locker token'),
        null=True,
        blank=True,
        unique=True,
        editable=False,
        help_text=_('Non-editable, to be generated by system itself and only when is_publish=True ,\
                    means when Process Locker is Published.'),
    )
    is_publish = models.BooleanField(
                    _('Publish Locker'),
                    default=False,
                    help_text=_('Only Publish When you are sure. Once published Locker cannot be updated.')
    )
    created_at = models.DateTimeField(
                 _('created at'),
                 auto_now_add=True,
                 db_index=True,
                 editable=False,
                 help_text = _('Non-editable, to be generated by system itself.'),
    )

    # this uuid may be used to access many processes
    # associated with it
    # each process may have a unique token associated to it
    # we'll do that in the through mapping
    processes = models.ManyToManyField(Process)

    # Meta
    class Meta:
        verbose_name = _("Process`s Locker")
        verbose_name_plural = _("Process`s Locker")
        ordering = ["-created_at"]

    # Functions
    def __str__(self):
        return "Process Locker {0}".format(self.name)

    def save(self, *args, **kwargs):
        """Override save() method to check if Locker is published if yes, then generate token for locker

        """
        if self.is_publish is True:
            self.token = str(uuid.uuid4())
        return super(ProcessLocker, self).save(*args, **kwargs)