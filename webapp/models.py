from django.db import models

# Create your models here.

class Task(models.Model):
   description = models.TextField(max_length=40, verbose_name='Описание')
   status = models.CharField(max_length=50, verbose_name='Статус', default='new')
   date_finish = models.DateField(verbose_name='Время выполнения', auto_now_add=True)

   def __str__(self):
      return f'{self.id}. {self.description}'