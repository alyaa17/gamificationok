from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'points', 'is_staff', 'id', 'test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6',
                    'test_7', 'test_8', 'art_2', 'art_3', 'art_4', 'art_5', 'art_6']


admin.site.register(CustomUser, CustomUserAdmin)
