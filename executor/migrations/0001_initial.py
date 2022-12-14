# Generated by Django 4.0.6 on 2022-07-31 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Menedj', 'Менеджер проекта'), ('Superv', 'Руководитель группы'), ('Execut', 'Исполнитель')], max_length=6, verbose_name='Должность')),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pict', verbose_name='Фотография')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ник пользователя')),
            ],
        ),
    ]
