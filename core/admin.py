
"""
Django admin costumisation
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name','level','owner']
    fieldsets = (
        (None, {"fields": ('email', 'password','level')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }

        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login','level']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
                'level'
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
