from django.contrib import admin

from tasks.models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'executor', 'file')

    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'executor', 'project', 'file')