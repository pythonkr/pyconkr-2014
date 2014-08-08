from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages import views
from .views import index, RoomDetail
from .views import SpeakerList, SpeakerDetail
from .views import SponsorList, SponsorDetail
from .views import ProgramList, ProgramDetail

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^room/(?P<pk>\d+)/$', RoomDetail.as_view(), name='room'),
    url(r'^speakers/$', SpeakerList.as_view(), name='speakers'),
    url(r'^speaker/(?P<slug>\w+)/$', SpeakerDetail.as_view(), name='speaker'),
    url(r'^sponsors/$', SponsorList.as_view(), name='sponsors'),
    url(r'^sponsor/(?P<slug>\w+)/$', SponsorDetail.as_view(), name='sponsor'),
    url(r'^programs/$', ProgramList.as_view(), name='programs'),
    url(r'^program/(?P<pk>\d+)/$', ProgramDetail.as_view(), name='program'),

    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# for development
urlpatterns += staticfiles_urlpatterns()

# for flatpages
urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]
