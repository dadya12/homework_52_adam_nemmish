import datetime
from django import forms
from .models import Task


class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'details_description', 'status', 'date_finish']

    def clean_due_date(self):
        date_finish = self.cleaned_data.get('due_date')
        if date_finish and date_finish < datetime.date.today():
            raise forms.ValidationError('Дедлайн не может быть в прошлом.')
        return date_finish