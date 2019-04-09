from django.shortcuts import render
from .models import Project, Sheet

def project_list(request):
    projects = Project.objects.all
    return render(request, 'parame/project/list.html', {'projects': projects})

def sheet_list(request, pk):
    sheets = Sheet.objects.filter(project=pk)
    return render(request, 'parame/sheet/list.html', {'sheets': sheets})