from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django_summernote.admin import SummernoteModelAdmin
from .models import Room, Program, ProgramTime, ProgramDate, Speaker, Sponsor


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
admin.site.register(Room, RoomAdmin)


class ProgramDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'day',)
admin.site.register(ProgramDate, ProgramDateAdmin)


class ProgramTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'begin', 'end',)
    ordering = ('begin',)
admin.site.register(ProgramTime, ProgramTimeAdmin)


class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name',)
    ordering = ('name',)
    search_fields = ('name',)
admin.site.register(Sponsor, SponsorAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name',)
    ordering = ('name',)
    search_fields = ('name',)
admin.site.register(Speaker, SpeakerAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'date', 'room')
    ordering = ('id',)
    filter_horizontal = ('times', )
    search_fields = ('name', 'speakers__name', 'desc',)
admin.site.register(Program, ProgramAdmin)


class FlatPageAdmin(SummernoteModelAdmin):
    pass


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
