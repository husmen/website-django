from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path("<int:pk>/", views.project_details, name="project_details"),
]
