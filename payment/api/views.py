from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from students.models import Student
from .serializer import *
from payment.models import StudentPayment
class StudentPaymentViewset(ModelViewSet):
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        print(user)
        try:
            student = Student.objects.get(id=data['student'])
            payment=StudentPayment.objects.create(student=student,cost=data['cost'],type=data['type'],description=data.get('description','Malumot berilmadi!'),user=user)
            serializer = StudentPaymentSerializer(data=payment,many=True)
            return Response('Succesfully!')
        except Exception as e:
            print(e)
            return Response('Error!')
    def partial_update(self, request, *args, **kwargs):
        payment_object = self.get_object()
        data = request.data
        user = request.user
        try:
            student = Student.objects.get(id=data['student'])
            payment_object.student =student
            payment_object.cost = data.get('cost',payment_object.cost)
            payment_object.description=data.get('description',payment_object.description)
            payment_object.user= user
            serializer = StudentPaymentSerializer(payment_object,partial=True)
            return Response('Succesfully!')
        except Exception as e:
            print(e)
            return Response('Error')
    def update(self, request, *args, **kwargs):
        return self.partial_update(request)
