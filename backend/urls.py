from django.urls import path
from .views import CvExperienceView, CvExperiencesViewEs


urlpatterns = [
    path('experiences/', CvExperiencesViewEs.as_view()),
    path('experiences/<int:pk>/', CvExperienceView.as_view()),
]
