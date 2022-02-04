import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """Was published recently should return False for questions whose
        pub_date is in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Is this a question?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)