from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')     # Shows these columns in the list view
    list_filter = ('publication_year', 'author')               # Adds filter sidebar for these fields
    search_fields = ('title', 'author')                        # Enables search by title or author


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff'
    )
    list_filter = (
        'is_staff', 'is_superuser', 'is_active', 'groups'
    )

    fieldsets = list(UserAdmin.fieldsets) + [
        (_('Additional Info'), {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    ]

    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        (_('Additional Info'), {
            'classes': ('wide',),
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    ]

    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
