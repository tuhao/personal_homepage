from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from users.views import *
import os.path

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vote.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^$',poll_detail),
    url(r'^poll/(\d+)/$',poll_detail),
    url(r'^(?P<poll_id>\d+)/results/$',results),
    url(r'^(?P<poll_id>\d+)/vote/$',vote),
    
)
