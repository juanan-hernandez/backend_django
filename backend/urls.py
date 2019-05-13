from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCvEmploymentHistory.as_view()),
    # path('', views.ListPlanes.as_view()),
    # path('<int:pk>/', views.DetailPlanes.as_view()),
]