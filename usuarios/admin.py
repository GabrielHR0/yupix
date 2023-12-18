from django.contrib import admin
from .models import UserRegister

class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birth_date', 'city', 'state')
    search_fields = ('first_name', 'last_name', 'email', 'city', 'state')

admin.site.register(UserRegister, UserRegisterAdmin)
