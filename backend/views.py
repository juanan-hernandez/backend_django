from django.shortcuts import render
from rest_framework import generics
from .models import CvExperience
from .serializers import CvExperienceSerializer


def index(request, path=''):
    return render(request, 'index.html')


class CvExperienceView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CvExperience.objects.all()
    serializer_class = CvExperienceSerializer


class CvExperiencesView(generics.ListCreateAPIView):

    queryset = CvExperience.objects.all()
    serializer_class = CvExperienceSerializer


