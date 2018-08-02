from django.forms.widget import Widget

class Stars(Widget):
    template_name = 'django_starfield/stars.html'

    def __init__(self, attrs=None, stars=5, codepoint='2605'):
        super(Stars, self).__init__(attrs)
        self.stars = 5
        self.codepoint = codepoint

    def get_context(self, name, value, attrs):
        context = super(Stars, self).get_context(name, value, attrs)
        context['stars'] = range(self.stars, 0, -1)
        return context
