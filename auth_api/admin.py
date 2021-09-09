from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from auth_api import models


class UserAdmin(BaseUserAdmin):
    """settings the appearance and fields to display in django admin page"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'),{'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('OTP Info'),{'fields': ('otp_code', 'otp_key',)}),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    
    #fields to show when adding user in django admin add page via the add button
    add_fieldsets = (
        (None, {

            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)