from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Room, Program, ProgramDate, Speaker, Sponsor


def index(request):
    return render(request, 'index.html')


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
