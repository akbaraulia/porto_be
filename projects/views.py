from django.shortcuts import render
from .models import Project
from django.http import JsonResponse

def project_list(request):
    projects = Project.objects.all()
    data = [
        {
            "id": project.id,
            "title": project.title,
            "description": project.description,
            "stack": project.stack,
            "link": project.link,
            "link_github": project.link_github,
            "foto1_url": request.build_absolute_uri(project.foto1.url) if project.foto1 else None,
            "foto2_url": request.build_absolute_uri(project.foto2.url) if project.foto2 else None,
            "foto3_url": request.build_absolute_uri(project.foto3.url) if project.foto3 else None,
        }
        for project in projects
    ]
    return JsonResponse(data, safe=False)