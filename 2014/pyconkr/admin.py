from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django_summernote.admin import SummernoteModelAdmin
from .models import (Room, Program, ProgramTime, ProgramDate, ProgramCategory,
                     Speaker, Sponsor, SponsorLevel,
                     Announcement, Jobfair)


class RoomAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)
    search_fields = ('name',)
admin.site.register(Room, RoomAdmin)


class ProgramDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'day',)
admin.site.register(ProgramDate, ProgramDateAdmin)


class ProgramTimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'begin', 'end',)
    list_editable = ('name',)
    ordering = ('begin',)
admin.site.register(ProgramTime, ProgramTimeAdmin)


class ProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_editable = ('name',)
admin.site.register(ProgramCategory, ProgramCategoryAdmin)


class SponsorAdmin(SummernoteModelAdmin):
    list_display = ('id', 'slug', 'name',)
    ordering = ('name',)
    list_editable = ('slug', 'name',)
    search_fields = ('name',)
admin.site.register(Sponsor, SponsorAdmin)


class SponsorLevelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'order', 'name',)
    list_editable = ('name', 'order',)
    ordering = ('order',)
    search_fields = ('name',)
admin.site.register(SponsorLevel, SponsorLevelAdmin)


class SpeakerAdmin(SummernoteModelAdmin):
    list_display = ('id', 'slug', 'name',)
    ordering = ('name',)
    search_fields = ('name', 'slug',)
admin.site.register(Speaker, SpeakerAdmin)


class ProgramAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'date', 'room', 'category',)
    list_editable = ('name', 'category',)
    ordering = ('id',)
    filter_horizontal = ('times', )
    search_fields = ('name', 'speakers__name', 'desc',)
admin.site.register(Program, ProgramAdmin)


class AnnouncementAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'created', 'modified')
    ordering = ('id',)
    search_fields = ('title',)
admin.site.register(Announcement, AnnouncementAdmin)


class JobfairAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'location', 'sponsor')
    list_editable = ('name', 'location', 'sponsor')
    ordering = ('id',)
    search_fields = ('name', 'sponsor__name')
admin.site.register(Jobfair, JobfairAdmin)


class FlatPageAdmin(SummernoteModelAdmin):
    pass


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
