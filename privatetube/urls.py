from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tube.views.index'),
    url(r'^upload/', 'tube.views.upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)$', 'tube.views.video'),
)
