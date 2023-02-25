from django.contrib import admin
from app.models import User,Calendar,Event,Invites
from app.forms import *
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email','username','name','is_staff',]
    list_display_links = ['username',]
    fieldsets = UserAdmin.fieldsets + ((None,{'fields' : ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields' : ("name",)}),)
admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(Invites)
