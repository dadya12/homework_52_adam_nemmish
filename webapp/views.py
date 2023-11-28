from django.shortcuts import render
from webapp.models import Task
# Create your views here.
def display_task(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def home(requset):
    return render(requset, 'home.html')