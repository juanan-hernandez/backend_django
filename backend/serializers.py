from rest_framework import serializers
from backend.models import CvExperience


class CvExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CvExperience
        fields = '__all__'
