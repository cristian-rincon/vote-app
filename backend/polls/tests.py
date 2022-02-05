import datetime
from typing import Any, Union

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question

SAMPLE_QUESTION = "¿Is this a question?"
SAMPLE_PAST_QUESTION = "¿Was this a question?"


def create_question(question_text: str, days: int) -> Union[Question, Any]:
    """
    Simple function to create a question with the given text and
    the given number of days offset to now. (negative for questions
    published in the past, positive for questions that have yet to be
    published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self) -> None:
        """Was published recently should return False for questions whose
        pub_date is in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text=SAMPLE_QUESTION, pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_not_published_recently(self) -> None:
        """Was published recently should return False for questions whose
        pub_date is older than 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(question_text=SAMPLE_QUESTION, pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self) -> None:
        """Was published recently should return True for questions whose
        pub_date is within the last day."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(question_text=SAMPLE_QUESTION, pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):

    INDEX_URL = "polls:index"

    def test_no_questions(self) -> None:
        """If no question exists, an appropiate message is displayed."""
        response = self.client.get(reverse(self.INDEX_URL))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self) -> None:
        """Questions with a pub_date in the future aren't displayed on the
        index page."""
        create_question(question_text=SAMPLE_QUESTION, days=30)
        response = self.client.get(reverse(self.INDEX_URL))
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self) -> None:
        """Questions with a pub_date in the past are displayed on the index
        page."""
        question = create_question(question_text=SAMPLE_PAST_QUESTION, days=-30)
        response = self.client.get(reverse(self.INDEX_URL))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])

    def test_future_question_and_past_question(self) -> None:
        """Even if both past and future questions exist, only past questions
        are displayed."""
        past_question = create_question(question_text=SAMPLE_PAST_QUESTION, days=-30)
        create_question(question_text=SAMPLE_QUESTION, days=30)
        response = self.client.get(reverse(self.INDEX_URL))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])

    def test_two_past_questions(self) -> None:
        """The questions index page may display multiple questions."""
        past_question_1 = create_question(question_text=SAMPLE_PAST_QUESTION, days=-29)
        past_question_2 = create_question(question_text=SAMPLE_PAST_QUESTION, days=-30)
        response = self.client.get(reverse(self.INDEX_URL))
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question_1, past_question_2])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self) -> None:
        """The detail view of a question with a pub_date in the future
        returns a 404 not found."""
        future_question = create_question(question_text=SAMPLE_QUESTION, days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self) -> None:
        """The detail view of a question with a pub_date in the past
        displays the question's text."""
        past_question = create_question(question_text=SAMPLE_PAST_QUESTION, days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
