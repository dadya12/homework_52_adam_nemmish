from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices
from webapp.validate import validate
from webapp.forms import TaskForms
# Create your views here.
def display_task(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def home(requset):
    return render(requset, 'home.html')

def tasks_views(requset, pk):
    tasks = get_object_or_404(Task, pk=pk)
    return render(requset, 'details_task.html', {'tasks': tasks})

def create_new(request):
    if request.method == "GET":
        form = TaskForms()
        return render(request, 'create_task.html', {'form': form})
    elif request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description = form.cleaned_data.get('description'),
                details_description = form.cleaned_data.get('details_description'),
                status = form.cleaned_data.get('status'),
                date_finish = form.cleaned_data.get('date_finish'),
            )
            return redirect('display_view', pk=task.pk)
        else:
            return render(request, 'create_task.html', {'form': form})

def update_new(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForms(initial={
            'description': task.description,
            'details_description': task.details_description,
            'status': task.status,
            'date_finish': task.date_finish
        })
        return render(request, 'update_task.html', {'form': form})
    elif request.method == "POST":
        form = TaskForms(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.details_description = form.cleaned_data.get('details_description')
            task.status = form.cleaned_data.get('status')
            task.date_finish = form.cleaned_data.get('date_finish')
            task.save()
            return redirect('display_view', pk=task.pk)
        else:
            task.save()
            return render(request, 'update_task.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('display_task')