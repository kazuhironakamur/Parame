from django.shortcuts import render, get_object_or_404
from .models import Project, Sheet

def project_list(request):
    projects = Project.objects.all
    return render(request, 'parame/project/list.html', {'projects': projects})

def sheet_list(request, pk):
    sheets = Sheet.objects.filter(project=pk)
    return render(request, 'parame/sheet/list.html', {'sheets': sheets})

def sheet_detail(request, pk, sk):
    sheet = get_object_or_404(Sheet, pk=sk)
    return render(request, 'parame/sheet/detail.html', {'sheet': sheet})