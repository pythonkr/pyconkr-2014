from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import (Room, Program, ProgramDate,
                     Speaker, Sponsor, Jobfair, Announcement)


def index(request):
    return render(request, 'index.html', {
        'recent_announcements': Announcement.objects.all()[:3],
    })


def schedule(request):
    return render(request, 'schedule.html')


class RoomDetail(DetailView):
    model = Room


class SponsorList(ListView):
    model = Sponsor


class SponsorDetail(DetailView):
    model = Sponsor


class SpeakerList(ListView):
    model = Speaker


class SpeakerDetail(DetailView):
    model = Speaker


class ProgramList(ListView):
    model = Program

    def get_context_data(self, **kwargs):
        context = super(ProgramList, self).get_context_data(**kwargs)
        context['dates'] = ProgramDate.objects.all()
        return context


class ProgramDetail(DetailView):
    model = Program


class JobfairList(ListView):
    model = Jobfair


class AnnouncementList(ListView):
    model = Announcement


class AnnouncementDetail(DetailView):
    model = Announcement
