from django.shortcuts import render
from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect
# Create your views here.
def display_task(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def home(requset):
    return render(requset, 'home.html')

def create_new(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {'status': status_choices})
    elif request.method == "POST":
        Task.objects.create(
            description= request.POST.get('description'),
            details_description=request.POST.get('details_description'),
            status= request.POST.get('status'),
            date_finish= request.POST.get('date_finish')
        )
        return HttpResponseRedirect('/')