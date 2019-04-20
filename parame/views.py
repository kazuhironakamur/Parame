from django.shortcuts import render, get_object_or_404
from .forms import ProjectForm, SheetForm
from .models import Project, Sheet
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user.id)
    return render(request, 'parame/project/list.html', {'projects': projects})

@login_required
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.id
            project.save()
            return redirect('project_list')

    else:
        form = ProjectForm()
    
    return render(request, 'parame/project/edit.html', {'form': form})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.owner = request.user.id
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'parame/project/edit.html', {'form': form})

def sheet_list(request, pk):
    sheets = Sheet.objects.filter(project=pk)
    return render(request, 'parame/sheet/list.html', {'sheets': sheets})

def sheet_detail(request, pk, sk):
    sheet = get_object_or_404(Sheet, pk=sk)
    return render(request, 'parame/sheet/detail.html', {'sheet': sheet})

def sheet_edit(request, pk, sk):
    sheet = get_object_or_404(Sheet, pk=pk)
    sheet.owner = request.user.id
    if request.method == "POST":
        form = SheetForm(request.POST, instance=sheet)
        if form.is_valid():
            sheet = form.save(commit=False)
            sheet.save()
            return redirect('sheet_detail', pk=sheet.project.pk, sk=sheet.pk)
    else:
        form = SheetForm(instance=sheet)
    return render(request, 'parame/sheet/edit.html', {'form': form})