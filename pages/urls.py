from django.urls import path
from .views import test_view, about_view

urlpatterns = [
    path('testing/', test_view, name="test"),  # Added a trailing slash for consistency
    path("", about_view, name="about"),
]
