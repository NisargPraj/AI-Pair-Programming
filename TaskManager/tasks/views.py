from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, 'index.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    task = Task()
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect(task_list)
    return render(request, 'add_task.html')

def complete_task(request):
    task_id = request.GET['task_id']
    task = get_object_or_404(Task, task_id=task_id)
    task.completed = True
    task.completed_at = timezone.now()
    task.save()
    return redirect(task_list)

def delete_task(request):
    task_id = request.GET['task_id']
    task = get_object_or_404(Task, task_id=task_id)
    task.delete()
    return redirect(task_list)