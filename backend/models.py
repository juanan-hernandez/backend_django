from django.db import models

# Create your models here.


class CvExperience(models.Model):

    id = models.AutoField(primary_key=True)
    init_date = models.DateField()
    end_date = models.DateField()
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    class Meta:
        db_table = "CVExperiences"
