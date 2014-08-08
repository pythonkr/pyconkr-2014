from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)

# for development
urlpatterns += staticfiles_urlpatterns()
