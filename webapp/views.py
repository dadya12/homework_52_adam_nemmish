from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect
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
        return render(request, 'create_task.html', {'status': status_choices})
    elif request.method == "POST":
        task = Task.objects.create(
            description= request.POST.get('description'),
            details_description=request.POST.get('details_description'),
            status= request.POST.get('status'),
            date_finish= request.POST.get('date_finish')
        )
        return redirect('display_view', pk=task.pk)