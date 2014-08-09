from django.core.urlresolvers import reverse
from django.db import models
from jsonfield import JSONField


class Room(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('room', args=[self.id])

    def __unicode__(self):
        return self.name


class ProgramDate(models.Model):
    day = models.DateField()

    def __unicode__(self):
        return self.day.strftime("%m/%d (%a)")


class ProgramTime(models.Model):
    name = models.CharField(max_length=100)
    begin = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return '%s - %s' % (self.begin, self.end)


class ProgramCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name


class SponsorLevel(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name


class Sponsor(models.Model):
    slug = models.SlugField(max_length=100, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='sponsor', null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    level = models.ForeignKey(SponsorLevel, null=True)

    def get_absolute_url(self):
        return reverse('sponsor', args=[self.slug])

    def __unicode__(self):
        return self.name


class Speaker(models.Model):
    slug = models.SlugField(max_length=100, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='sponsor', null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    info = JSONField()

    def get_absolute_url(self):
        return reverse('speaker', args=[self.slug])

    def __unicode__(self):
        return '%s(%s)' % (self.name, self.slug)


class Program(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(null=True, blank=True)
    slide_url = models.CharField(max_length=255, null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, blank=True)

    room = models.ForeignKey(Room)
    date = models.ForeignKey(ProgramDate)
    times = models.ManyToManyField(ProgramTime)
    category = models.ForeignKey(ProgramCategory, null=True)

    def get_absolute_url(self):
        return reverse('program', args=[self.id])

    def begin_time(self):
        return self.times.all()[0].begin.strftime("%H:%M")

    def get_times(self):
        times = self.times.all()
        return '%s - %s' % (times[0].begin.strftime("%H:%M"),
                            times[len(times) - 1].end.strftime("%H:%M"))

    def __unicode__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Jobfair(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    sponsor = models.ForeignKey(Sponsor, null=True)
    desc = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name