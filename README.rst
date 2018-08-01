Django stars widget
===================

Description
-----------

This is a simple widget rendering so-called rating stars as input for an
integer field. It is based solely on CSS 3, as laid out by `Martin Ivanov
<http://experiments.wemakesites.net/css3-rating-stars-with-selection.html>`_.

Usage
-----

Just add the Stars widget to any IntegerField in a Django form.

.. code:: python

  from django import forms
  from django_starfield import Stars

  class StarsExampleForm(forms.Form):
      rating = forms.IntegerField(widget=Stars())

You can change the number of stars by passing the stars argument to the
Stars widget.

Differences
-----------

This is different from other star rating applications in that it provides
only a widget returning its selction to any IntegerField. It is not a
complete rating application, just a presentational widget for integer input.
