from django.urls import path
from.views import test_view, about_view


urlpattern = [
    path('testing', test_view, name="test"),
    path("", about_view, name="about"),
]
    
