from django.contrib import admin

from executor.models import Executor

@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'photo')
