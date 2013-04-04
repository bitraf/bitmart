from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'clerk.views.clerk'),

    url(r'^products/$', 'clerk.views.products'),
    url(r'^products/(?P<product_id>\d+)/$', 'clerk.productdetail.edit'),
    url(r'^products//$', 'clerk.productdetail.new'),


    url(r'^supplies/$', 'clerk.supplies.restock'),
)
