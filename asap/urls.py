"""veris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers
from rest_framework_swagger.views import get_swagger_view

from asap.apps.organizations.views import MemberViewSet
from .router import Router

schema_view = get_swagger_view(title='Veris Organizations API')

routes_organization = routers.NestedSimpleRouter(Router.shared_router, 'organizations', lookup='organization')
routes_organization.register('members', MemberViewSet, base_name='organizations')

urlpatterns = [
    url(r'^swagger/$', schema_view),
    url(r'^api/v1/', include(Router.shared_router.urls)),
    url(r'^api/v1/', include(routes_organization.urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    # we have our own oauth provider
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^api/auth/', include('asap.apps.authentication.urls', namespace='auth')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
