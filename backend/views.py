# from django.shortcuts import render
from rest_framework import generics
from .models import CvExperience
from .serializers import CvExperienceSerializer, CvExperienceSerializerEn, CvExperienceSerializerEs


class CvExperienceView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CvExperience.objects.all()
    serializer_class = CvExperienceSerializer


class CvExperiencesViewEn(generics.ListCreateAPIView):

    queryset = CvExperience.objects.all().order_by('-init_date')
    serializer_class = CvExperienceSerializerEn


class CvExperiencesViewEs(generics.ListCreateAPIView):

    queryset = CvExperience.objects.all().order_by('-init_date')
    serializer_class = CvExperienceSerializerEs
