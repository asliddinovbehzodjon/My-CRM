from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from students.models import *
class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context