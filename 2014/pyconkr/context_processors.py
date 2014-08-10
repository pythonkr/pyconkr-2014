from django.core.urlresolvers import resolve
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict
from .models import Sponsor


def menu(request):
    menu = OrderedDict([
        ('about', {
            'title': _('About'),
            'icon': 'python',
            'dropdown': OrderedDict([
                ('pyconkr', {'title': _('About Pycon Korea')}),
                ('detail', {'title': _('Conference detail')}),
                ('announcements', {'title': _('Announcements')}),
                ('sponsors', {'title': _('Sponsors')}),
                ('staff', {'title': _('Staff')}),
            ]),
        }),
        ('programs', {
            'title': _('Program'),
            'icon': 'calendar',
            'dropdown': OrderedDict([
                ('cfp', {'title': _('Call for proposal')}),
                ('schedule', {'title': _('Schedule')}),
                ('', {'title': _('Programs')}),
                ('speakers', {'title': _('Speakers')}),
                ('jobfair', {'title': _('Jobfair')}),
                ('bof', {'title': _('BOF')}),
            ]),
        }),
        ('registration', {
            'title': _('Registration'),
            'icon': 'pencil',
        }),
        ('venue', {
            'title': _('Venue'),
            'icon': 'map-marker',
        }),
        ('contact', {
            'title': _('Contact'),
            'icon': 'info-sign',
        }),
    ])

    try:
        name = resolve(request.path).url_name
        if name in menu:
            menu[name]['active'] = True
    except:
        pass

    return {
        'menu': menu,
    }


def sponsors(request):
    sponsors = Sponsor.objects.all()

    return {
        'sponsors': sponsors,
    }
