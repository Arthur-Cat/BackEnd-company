from django.db import models
from executor.models import Executor

class Subdivision(models.Model):
    name_subdiv = models.CharField(max_length=20, verbose_name='Имя подразделения')    
    manager = models.OneToOneField(Executor, on_delete=models.CASCADE, verbose_name='Менеджер проекта')

    def __str__(self):
        return self.name_subdiv

class GroupExecut(models.Model):
    JOBS = (
        ('Back', 'BackEnd'),
        ('Front', 'FrontEnd'),
        ('Fillst', 'FullStak'),
    )
    job = models.CharField(max_length=6, choices=JOBS, verbose_name='Направление')
    name_group = models.CharField(max_length=20, verbose_name='Имя группы')
    sibdivi = models.ForeignKey(Subdivision, on_delete=models.CASCADE, verbose_name='Подразделение')
    execut = models.ManyToManyField(Executor, verbose_name='Участники группы')
    def __str__(self):
        return self.name_group