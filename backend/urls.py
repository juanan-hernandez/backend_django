from django.urls import path
from .views import CvExperienceView, CvExperiencesView


urlpatterns = [
    path('', CvExperiencesView.as_view()),
    path('<int:pk>/', CvExperienceView.as_view()),
]