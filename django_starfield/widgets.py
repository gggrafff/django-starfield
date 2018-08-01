from django.forms.widget import Widget

class Stars(Widget):
    template_name = 'django_starfield/stars.html'

    def __init__(self, attrs=None, stars=5):
        super(Stars, self).__init__(attrs)
        self.stars = 5

    def get_context(self, name, value, attrs):
        context = super(Stars, self).get_context(name, value, attrs)
        context['stars'] = self.stars
        return context
