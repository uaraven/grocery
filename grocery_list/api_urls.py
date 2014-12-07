from django.conf.urls import patterns, url

from grocery_list import api_views


urlpatterns = patterns('',
    url(r'^list', api_views.get_list),
    url(r'^add', api_views.add_list_item),
    url(r'^done', api_views.set_done),
    url(r'^suggest', api_views.suggest),
    url(r'^delete', api_views.delete),
)
