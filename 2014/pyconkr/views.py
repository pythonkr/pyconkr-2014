from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import (Room,
                     Program, ProgramDate, ProgramTime, ProgramCategory,
                     Speaker, Sponsor, Jobfair, Announcement)


def index(request):
    return render(request, 'index.html', {
        'recent_announcements': Announcement.objects.all()[:3],
    })


def schedule(request):
    dates = ProgramDate.objects.all()
    times = ProgramTime.objects.all()
    rooms = Room.objects.all()

    wide = {}
    narrow = {}
    processed = set()
    for d in dates:
        wide[d] = {}
        narrow[d] = {}
        for t in times:
            wide[d][t] = {}
            narrow[d][t] = {}
            for r in rooms:
                s = Program.objects.filter(date=d, times=t, rooms=r)
                if s:
                    if s[0].times.all()[0] == t and s[0].id not in processed:
                        wide[d][t][r] = s[0]
                        narrow[d][t][r] = s[0]
                        processed.add(s[0].id)
                else:
                    wide[d][t][r] = None

            if len(narrow[d][t]) == 0:
                del(narrow[d][t])

    contexts = {
        'wide': wide,
        'narrow': narrow,
        'rooms': rooms,
    }
    return render(request, 'schedule.html', contexts)


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
    model = ProgramCategory
    template_name = "pyconkr/program_list.html"


class ProgramDetail(DetailView):
    model = Program


class JobfairList(ListView):
    model = Jobfair


class AnnouncementList(ListView):
    model = Announcement


class AnnouncementDetail(DetailView):
    model = Announcement
