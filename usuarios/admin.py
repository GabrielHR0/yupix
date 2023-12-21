from django.contrib import admin
from .models import UserRegister, ServerRegister

class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birth_date', 'city', 'state')
    search_fields = ('first_name', 'last_name', 'email', 'city', 'state')

class ServerRegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'service', 'document', 'birth_date', 'city', 'state')
    search_fields = ('first_name', 'last_name', 'email', 'city', 'state')

admin.site.register(UserRegister, UserRegisterAdmin)
admin.site.register(ServerRegister, ServerRegisterAdmin)
