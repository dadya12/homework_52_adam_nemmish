"""
URL configuration for task1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import display_task, home, create_new, tasks_views, update_new, task_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks/', display_task, name='display_task'),
    path('add_task/', create_new, name='create_new'),
    path('details/<int:pk>/', tasks_views, name='display_view'),
    path('update/<int:pk>/', update_new, name='update_task'),
    path('delete_task/<int:pk>/', task_delete, name='task_delete')
]
