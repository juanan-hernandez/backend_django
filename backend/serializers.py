from rest_framework import serializers
from backend.models import CvExperience


class CvExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CvExperience
        fields = '__all__'


class CvExperienceSerializerEn(serializers.ModelSerializer):

    class Meta:
        model = CvExperience
        fields = ('id',
                  'init_date',
                  'end_date',
                  'country_en',
                  'city_en',
                  'company',
                  'role_en',
                  'description_en')


class CvExperienceSerializerEs(serializers.ModelSerializer):

    class Meta:
        model = CvExperience
        fields = ('id',
                  'init_date',
                  'end_date',
                  'country_es',
                  'city_es',
                  'company',
                  'role_es',
                  'description_es')

