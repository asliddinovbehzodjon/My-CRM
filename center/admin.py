from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *
class MyAdmin(UserAdmin):
    list_filter = ['role','is_active','is_staff','is_superuser']
    list_display = ['role','username','email','is_staff','is_superuser']
admin.site.register(User,MyAdmin)
class DirectorAdmin(UserAdmin):
    list_filter = ['role','is_active']
    model = Director
    add_form =DirectorForm
admin.site.register(Director,DirectorAdmin)
class ManagerAdmin(UserAdmin):
    list_filter = ['role','is_active']
    model = Manager
    add_form =ManagerForm
    
admin.site.register(Manager,ManagerAdmin)
class TeacherAdmin(UserAdmin):
    list_filter = ['role','is_active']
    model = Teacher
    add_form =TeacherForm
    
admin.site.register(Teacher,TeacherAdmin)
