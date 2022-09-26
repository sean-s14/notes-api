from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from .models import Task


class TaskAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('text', 'completed')}),
    )
    list_display = ('text', 'completed')


admin.site.register(Task, TaskAdmin)