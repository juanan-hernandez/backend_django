from rest_framework import generics
from .models import CvExperience
from .serializers import CvExperienceSerializer


class CvExperienceView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CvExperience.objects.all()
    serializer_class = CvExperienceSerializer


class CvExperiencesView(generics.ListCreateAPIView):

    queryset = CvExperience.objects.all()
    serializer_class = CvExperienceSerializer


