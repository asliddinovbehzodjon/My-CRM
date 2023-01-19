from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from center.models import *
class DirectorViewset(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
class ManagerViewset(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
