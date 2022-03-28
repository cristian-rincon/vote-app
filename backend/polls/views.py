# Django REST Framework
from rest_framework import viewsets

from .models import Choice, Question
from .serializers import ChoiceSerializer, QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """

    queryset = Question.objects.all().order_by("-pub_date")
    serializer_class = QuestionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows choices to be viewed or edited.
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    # permission_classes = [permissions.IsAuthenticated]
