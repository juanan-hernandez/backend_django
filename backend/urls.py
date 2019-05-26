from django.urls import path
from .views import CvExperienceView, CvExperiencesViewEn, CvExperiencesViewEs


urlpatterns = [
    path('experiences/', CvExperiencesViewEs.as_view()),
    path('experiences/<int:pk>/', CvExperienceView.as_view()),
]
