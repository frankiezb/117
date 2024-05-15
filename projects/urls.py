from django.urls import path
from.views import projects__views

urlpatters = [
    path("", projects__views, name="projects")
]