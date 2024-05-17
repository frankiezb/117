from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_view(request):
    
    projects = Project.objects.all()  # corrected "objects" instead of "object"
    return render(request, 'projects/projects.html', {
        'projects': projects                                                      
    })
