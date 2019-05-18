from django.db import models

# Create your models here.


class CvExperience(models.Model):

    id = models.AutoField(primary_key=True)
    init_date = models.DateField()
    end_date = models.DateField()
    country_en = models.CharField(max_length=128)
    country_es = models.CharField(max_length=128)
    city_en = models.CharField(max_length=128)
    city_es = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    role_en = models.CharField(max_length=128)
    role_es = models.CharField(max_length=128)
    description_en = models.CharField(max_length=1024)
    description_es = models.CharField(max_length=1024)

    class Meta:
        db_table = "cv_experiences"
