from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
# Create your models here.
class Task(models.Model):
   description = models.TextField(max_length=40, verbose_name='Описание')
   details_description = models.TextField(max_length=50, verbose_name='Подробное описание', null=True, blank=True)
   status = models.CharField(max_length=50, verbose_name='Статус', default='new', choices=status_choices)
   date_finish = models.DateField(verbose_name='Время выполнения', null=True, blank=True)

   def __str__(self):
      return f'{self.id}. {self.description}'