from django.urls import path
from .views import projects_view  # Corrected the import statement for projects_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [  # Corrected the variable name from urlpatters to urlpatterns
    path("", projects_view, name="projects"),  # Corrected projects_views to projects_view
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
