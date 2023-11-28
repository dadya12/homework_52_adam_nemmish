from django.contrib import admin
from webapp.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_finish']
    list_filter = ['status']
    search_fields = ['id', 'date_finish']
    fields = ['description', 'status', 'date_finish']
    readonly_fields = ['date_finish']