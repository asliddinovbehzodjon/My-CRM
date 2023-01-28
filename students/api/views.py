from django.shortcuts import render
from rest_framework.response import Response
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
class DavomatViewset(ModelViewSet):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        if 'students' in data:

            for student in data['students']:
                try:
                    talaba = Student.objects.get(id=student['id'])
                    print(talaba.name)
                    Davomat.objects.create(student=talaba,status=student['status'],description=student.get('description','Sabab korsatilmagan'))
                except Student.DoesNotExist:
                    pass
            return Response("Davomat olindi!")
        else:
            return Response('Student Doesnt Found')
    def partial_update(self, request, *args, **kwargs):
        davomat_data = self.get_object()
        data = request.data
        if 'students' in data:
           for student in data['students']:
                try:
                    student = Student.objects.get(id=student['id'])
                    davomat_data.student =student
                    davomat_data.description = student.get('description',davomat_data.description)
                    davomat_data.status = student.get('status',davomat_data.status)
                    davomat_data.date = student.get('date',davomat_data.date)
                    serializer = DavomatSerializer(davomat_data)
                    return Response(serializer.data)
                except Student.DoesNotExist:
                    return Response('Student not found')
        else:
            return Response('student field required')
    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
            
        
        
