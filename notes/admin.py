from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from .models import Note


class NoteAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'date_created', 'text')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'code', 'imageURI')}),
    #     (_('Permissions'), {
    #         'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), # 'session_id', 
    #     }),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'password1', 'password2'),
    #     }),
    )
    # list_filter = ('is_staff', 'is_active', 'is_verified')
    list_display = ('title', 'date_created')


admin.site.register(Note, NoteAdmin)