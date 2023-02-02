from django.db import models
from students.models import Student
from center.models import User
# Create your models here.
class StudentPayment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True)
    cost = models.CharField(max_length=500)
    payment_types = (
        ('naqd',"Naqd"),
        ("plastik","Plastik"),
        ("pul ko'chirish","Pul ko'chirish")
    )
    type = models.CharField(max_length=100,choices=payment_types)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Payment"

