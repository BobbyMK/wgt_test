from rest_framework import generics
from rest_framework import permissions

from survey.models import Survey
from survey.serializers import SurveySerializer

class SurveyAPIListCreate(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)