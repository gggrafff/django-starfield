from django.config import settings
from django.forms.widgets import Widget

from . import defaults

settings.configure(default_settings=defaults)

class Stars(Widget):
    template_name = 'django_starfield/stars.html'

    def __init__(self, attrs=None, stars=None, codepoint=None, colour=None):
        super(Stars, self).__init__(attrs)

        if stars is None:
            self.stars = settings.STARFIELD_STARS
        if codepoint is None:
            self.codepoint = settings.STARFIELD_CODEPOINT
        if colour is None:
            self.colour = settings.STARFIELD_COLOUR

    def get_context(self, name, value, attrs):
        context = super(Stars, self).get_context(name, value, attrs)
        context['stars'] = range(self.stars, 0, -1)
        if not self.codepoint == defaults.STARFIELD_CODEPOINT:
            context['codepoint'] = self.codepoint
        if not self.colour == defaults.STARFIELD_COLOUR:
            contect['colour'] = self.colour
        return context
