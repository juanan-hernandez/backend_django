from django.urls import path
from .views import CvExperienceView, CvExperiencesViewEn, CvExperiencesViewEs


urlpatterns = [
    path('', CvExperiencesViewEs.as_view()),
    path('<int:pk>/', CvExperienceView.as_view()),
]