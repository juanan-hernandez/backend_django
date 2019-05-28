# from django.shortcuts import render
from rest_framework import generics
from .models import CvExperience
from .serializers import CvExperienceSerializer, CvExperienceSerializerEn, CvExperienceSerializerEs


class CvExperienceView(generics.RetrieveAPIView):

    queryset = CvExperience.objects.all()
    serializer_class = CvExperienceSerializer


class CvExperiencesViewEn(generics.ListAPIView):

    queryset = CvExperience.objects.all().order_by('-init_date')
    serializer_class = CvExperienceSerializerEn


class CvExperiencesViewEs(generics.ListAPIView):

    queryset = CvExperience.objects.all().order_by('-init_date')
    serializer_class = CvExperienceSerializerEs

