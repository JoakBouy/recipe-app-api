"""Django Admin configuration for core app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models

class UserAdmin(BaseUserAdmin):
    """Define admin model for custom User model with no email field."""

    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)