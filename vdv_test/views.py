from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *

from vdv_test.models import Project


# Create your views here.

def get_projects(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()
    return render(request, 'vdv_test/GetAllProject.html', {'projects': projects})


def crate_project(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project()
            project.title = form.cleaned_data['title']
            project.description = form.cleaned_data['description']
            project.email = form.cleaned_data['email']
            project.countUsers = form.cleaned_data['countUsers']
            project.save()
            return HttpResponseRedirect('/vdv_test/')
    else:
        form = ProjectForm()
    return render(request, 'vdv_test/CreateProject.html', {'form': form})


def delete_project(request: HttpRequest, project_id: int) -> HttpResponse:
    project = Project.objects.get(id=project_id)
    project.delete()
    return HttpResponseRedirect('/vdv_test/')




def update_project(request: HttpRequest, project_id: int) -> HttpResponse:
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST)
        if form.is_valid():
            project.title = form.cleaned_data['title']
            project.email = form.cleaned_data['email']
            project.save()
            return HttpResponseRedirect('/vdv_test/')
    else:
        form = ProjectUpdateForm()
        form.fields['title'].initial = project.title
        form.fields['email'].initial = project.email
    return render(request, 'vdv_test/UpdateProject.html', {'form': form})