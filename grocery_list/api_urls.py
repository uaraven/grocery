from django.conf.urls import patterns, url
from grocery_list import api_views

urlpatterns = patterns('',
    url(r'^list', api_views.get_list),
    url(r'^add', api_views.add_list_item),
    url(r'^done/(?P<item_id>[0-9]*)/(?P<checked>\w*)/$', api_views.set_done)
)
