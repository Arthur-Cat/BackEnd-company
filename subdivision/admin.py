from django.contrib import admin

from subdivision.models import GroupExecut, Subdivision


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name_subdiv', 'manager')


@admin.register(GroupExecut)
class GroupExecutAdmin(admin.ModelAdmin):
    list_display = ('name_group', 'sibdivi', 'job')