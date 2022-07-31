from django.db import models
from django.conf import settings
from PIL import Image
from django.contrib.auth.models import User
"""Менеджер проектов, к нему будет идти привязка до 5 групп"""
"""Группы, в составе 4 СВ и 4 подгруппы с 10 исполнителями в каждой"""
"""Получается что в проекте будет 3 Менеджера к каждому 5 групп
в 1 группе будет 4 св и у каждого своя подгруппа и исполнителями по 10 человек"""
User
class Executor(models.Model):

    POSITIONS = [
        ('Menedj', 'Менеджер проекта'),
        ('Superv', 'Руководитель группы'),
        ('Execut', 'Исполнитель'),
    ]
    position = models.CharField(max_length=6, choices=POSITIONS, verbose_name='Должность')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Ник пользователя')
    photo = models.ImageField(upload_to='profile_pict', default='default.jpg', blank=True, verbose_name='Фотография')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='День рождения')

    def __str__(self):
        return self.user.username
    
    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

"""1) привязка к менеджеру, 2) название подразделения """

