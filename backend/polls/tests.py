from rest_framework.test import APITestCase

from .models import Question

SAMPLE_QUESTION = "¿Is this a question?"
SAMPLE_PAST_QUESTION = "¿Was this a question?"


class QuestionTests(APITestCase):
    def test_create_question(self) -> None:
        """
        Ensure we can create a new question object.
        """
        url = "/apiv1/questions/"
        data = {"question_text": SAMPLE_QUESTION, "pub_date": "2020-01-01T00:00:00Z"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().question_text, SAMPLE_QUESTION)
