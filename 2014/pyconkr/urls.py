from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.flatpages import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import index, schedule
from .views import RoomDetail, JobfairList
from .views import AnnouncementList, AnnouncementDetail
from .views import SpeakerList, SpeakerDetail
from .views import SponsorList, SponsorDetail
from .views import ProgramList, ProgramDetail

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^room/(?P<pk>\d+)$', RoomDetail.as_view(), name='room'),
    url(r'^about/announcements/$', AnnouncementList.as_view(), name='announcements'),
    url(r'^about/announcement/(?P<pk>\d+)$', AnnouncementDetail.as_view(), name='announcement'),
    url(r'^about/sponsors/$', SponsorList.as_view(), name='sponsors'),
    url(r'^about/sponsor/(?P<slug>\w+)$', SponsorDetail.as_view(), name='sponsor'),
    url(r'^programs/$', ProgramList.as_view(), name='programs'),
    url(r'^program/(?P<pk>\d+)$', ProgramDetail.as_view(), name='program'),
    url(r'^programs/speakers/$', SpeakerList.as_view(), name='speakers'),
    url(r'^programs/speaker/(?P<slug>\w+)$', SpeakerDetail.as_view(), name='speaker'),
    url(r'^programs/schedule/$', schedule, name='schedule'),
    url(r'^programs/jobfair/$', JobfairList.as_view(), name='jobfair'),

    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# for development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT})
    ]

# for rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]

# for flatpages
urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]
