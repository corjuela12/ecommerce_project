# Register your models here.
from django.contrib import admin
from .models import Profile

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):#cambio propio
    list_display = ('email', 'username', 'name', 'lastname', 'is_active', 'is_staff')
