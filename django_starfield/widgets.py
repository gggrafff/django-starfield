from django.conf import settings
from django.forms.widgets import Widget
import random
import string

STARFIELD_COLOUR = '#f5b301'
STARFIELD_CODEPOINT = '2605'
STARFIELD_STARS = 5
STARFIELD_TEMPLATE = 'django_starfield/stars.html'

class Stars(Widget):
    template_name = getattr(settings, 'STARFIELD_TEMPLATE', STARFIELD_TEMPLATE)

    def __init__(self, attrs=None, stars=None, codepoint=None, colour=None, unique_id=None):
        super(Stars, self).__init__(attrs)

        self.stars = stars if stars else getattr(settings, 'STARFIELD_STARS', STARFIELD_STARS)
        self.codepoint = codepoint if codepoint else getattr(settings, 'STARFIELD_CODEPOINT', STARFIELD_CODEPOINT)
        self.colour = colour if colour else getattr(settings, 'STARFIELD_COLOUR', STARFIELD_COLOUR)
        self.unique_id = unique_id if unique_id else ''.join([random.choice(string.ascii_lowercase) for i in range(8)])

    def get_context(self, name, value, attrs):
        context = super(Stars, self).get_context(name, value, attrs)
        context['stars'] = range(self.stars, 0, -1)
        context['unique_id'] = self.unique_id
        if not self.codepoint == STARFIELD_CODEPOINT:
            context['codepoint'] = self.codepoint
        if not self.colour == STARFIELD_COLOUR:
            context['colour'] = self.colour
        return context
