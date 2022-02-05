import datetime
from typing import Any, Union

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    published = models.BooleanField(default=False)

    def __str__(self) -> Union[str, Any]:
        return self.question_text

    def was_published_recently(self) -> Union[bool, Any]:
        """Tell if the question was published recently or not"""
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def count_of_votes(self) -> Union[int, Any]:
        """Count the number of votes for the question"""
        return self.choice_set.count()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> Union[str, Any]:
        return self.choice_text
