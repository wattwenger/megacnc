from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Cell, Project
# Create your views here.

def delete_cell(request, cell_id):
    cell = get_object_or_404(Cell, id=cell_id)
    cell.delete()
    messages.success(request, 'Cell deleted successfully.')
    return redirect('project_detail', project_id=cell.project.id)

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, 'Project and its database deleted successfully.')
    return redirect('projects_list')
