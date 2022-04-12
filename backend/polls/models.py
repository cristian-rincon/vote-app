import datetime
from typing import Any, Union

from django.db import models
from django.utils import timezone


class Question(models.Model):
    created_by = models.ForeignKey("auth.User", related_name="questions", on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True, blank=True)
    published = models.BooleanField(default=True)

    def __str__(self) -> Any:
        return self.question_text

    def was_published_recently(self) -> Any:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) and self.published


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> Union[str, Any]:
        return self.choice_text
