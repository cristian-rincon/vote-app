from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APITestCase

from .models import Question

SAMPLE_QUESTION = "¿Is this a question?"
SAMPLE_PAST_QUESTION = "¿Was this a question?"


def create_fake_user(username: str) -> None:
    user = User.objects.create(username=username)
    user.set_password("password")
    user.save()


class QuestionTestCase(APITestCase):
    def setUp(self) -> None:
        create_fake_user("user1")
        self.client.login(username="user1", password="password")  # nosec

    def test_create_question(self) -> None:
        self._extracted_from_test_create_question_with_invalid_data_2(SAMPLE_QUESTION, 201, 1)

        self.assertEqual(Question.objects.get().question_text, SAMPLE_QUESTION)

    def test_create_question_with_invalid_data(self) -> None:
        self._extracted_from_test_create_question_with_invalid_data_2("", 400, 0)

    # TODO Rename this here and in `test_create_question` and `test_create_question_with_invalid_data`
    def _extracted_from_test_create_question_with_invalid_data_2(self, question_text: str, response_status: int, object_count: int) -> None:
        data = {"question_text": question_text}
        response = self.client.post("/api/v1/questions/", data, format="json")
        self.assertEqual(response.status_code, response_status)
        self.assertEqual(Question.objects.count(), object_count)

    def test_was_published_recently_with_published_set_to_false(self) -> None:
        future_question = Question.objects.create(
            id=1, created_by=User(1), question_text=SAMPLE_QUESTION, pub_date=timezone.now() - timedelta(days=30), published=False
        )
        future_question.save()

        self.assertIs(future_question.was_published_recently(), False)
