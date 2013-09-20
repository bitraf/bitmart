from django.conf.urls import patterns, include, url
from django.shortcuts import redirect
from bitmart import settings
from cashregister.api import ProductResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

product_resource = ProductResource()

urlpatterns = patterns('',
    url(r'^store/', include('cashregister.urls')),
    url(r'^clerk/', include('clerk.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.RESOURCES_ROOT}),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(product_resource.urls)),

    (r'^app/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.FRONTEND_ROOT}),
)
