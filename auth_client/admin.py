from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Users)
class Users(ImportExportModelAdmin):
    list_display = ("email", "first_name")


@admin.register(UsersCows)
class UsersCows(ImportExportModelAdmin):
    list_display = ("name", "description")


@admin.register(UsersCalves)
class UsersCalves(ImportExportModelAdmin):
    list_display = ("calf_user", "calf_breed")
