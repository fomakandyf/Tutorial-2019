"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from django.utils import timezone

from .models import Question

def test_was_published_recently_with_future_question(self):
    time = timezone.now + datetime.timedelta(dadict_keys=30)
    future_question = Question(pub_date=time)
    self.assertIs(future_question.was_published_recently_recently(), False)
