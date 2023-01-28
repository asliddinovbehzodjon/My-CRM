from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','cost']
    list_filter = ['cost']
    search_fields = ['cost','name']
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','student_count']
    list_filter = ['student_count']
    search_fields = ['name','student_count']
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','user']
    search_fields = ['name']
