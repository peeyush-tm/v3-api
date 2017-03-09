#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- process.routers
~~~~~~~~~~~~~~~~~

- This file contains process routers.
"""

# Django
from django.conf.urls import include, url

# own app
from asap.apps.process.views import ProcessViewSet, ProcessLockerViewSet
from asap.apps.process.views.store_service import ResourceProxyViewSet
from asap.router import Router

from rest_framework_nested import routers

router = Router()
router.register('process-lockers', ProcessLockerViewSet, base_name='processlocker')
router.register('processes', ProcessViewSet, base_name='process')

routes_process = routers.NestedSimpleRouter(Router.shared_router, 'process-lockers', lookup='process_locker')
routes_process.register('processes', ProcessViewSet, base_name='process-lockers')

UUID_REGEX = '[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}'

process_resolve = ResourceProxyViewSet.as_view({
    'post': 'process_resolve',
})

urlpatterns = [
    url('', include(routes_process.urls)),
    url(r'^processes/(?P<uuid>{uuid})/resolve/$'.format(uuid=UUID_REGEX),
        process_resolve, name='process-resolve'),
]
