from django.db import models
from executor.models import Executor



class Project(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название проекта')
    body = models.TextField(max_length=150, verbose_name='Краткое описание')
    file = models.FileField(upload_to='file_save', verbose_name='Файл с проектом')
    create = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, verbose_name='Исполнитель')

    def __str__(self):
        return self.title


class Task(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название задачи')
    body = models.TextField(max_length=150, verbose_name='Краткое описание')
    file = models.FileField(upload_to='file_save', verbose_name='Файл с задачей', null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, verbose_name='Исполнитель')

    def __str__(self):
        return self.title