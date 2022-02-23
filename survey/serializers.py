from rest_framework import serializers
from survey.models import Survey

class SurveySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Survey
        fields = ('__all__')