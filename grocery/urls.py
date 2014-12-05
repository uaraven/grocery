from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grocery.views.home', name='home'),
    url(r'^api/', include('grocery_list.api_urls')),

    url(r'^admin/', include(admin.site.urls)),
)
