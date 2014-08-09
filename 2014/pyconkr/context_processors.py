from django.core.urlresolvers import resolve
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict


def menu(request):
    menu = OrderedDict([
        ('about', {
            'title': _('About'),
            'dropdown': OrderedDict([
                ('pyconkr', {'title': _('About Pycon KR')}),
                ('detail', {'title': _('Conference detail')}),
                ('sponsors', {'title': _('Sponsors')}),
                ('staff', {'title': _('Pycon KR team and staff')}),
            ]),
        }),
        ('programs', {
            'title': _('Program'),
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
        }),
        ('venue', {
            'title': _('Venue'),
        }),
        ('contact', {
            'title': _('Contact'),
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
