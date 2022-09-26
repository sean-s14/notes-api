from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from .models import Note


class NoteAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'date_created', 'text')}),
    )
    list_display = ('title', 'date_created')


admin.site.register(Note, NoteAdmin)