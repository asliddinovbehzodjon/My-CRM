from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
class DirectorForm(UserCreationForm):
    class Meta:
        model = Director
        fields = "__all__"
class ManagerForm(UserCreationForm):
    class Meta:
        model = Manager
        fields = "__all__"
class TeacherForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = "__all__"