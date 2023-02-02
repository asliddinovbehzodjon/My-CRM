from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','phone','parent','email']
    list_filter = ['language','added']
    search_fields = ['name','phone','mother_name','parent','father_name','email']
    list_per_page = 10
    list_editable = ['phone']
admin.site.register([Davomat,Test])
