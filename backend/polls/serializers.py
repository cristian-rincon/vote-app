from rest_framework import serializers

from .models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["question", "url", "choice_text", "votes"]


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "url", "question_text", "pub_date", "published", "choices", "created_by"]
