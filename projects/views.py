from django.shortcuts import render
from .models import Project
from django.http import JsonResponse

def project_list(request):
    projects = Project.objects.all()
    data = [{"title": project.title, "description": project.description} for project in projects]
    return JsonResponse(data, safe=False)
