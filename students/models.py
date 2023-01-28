from django.db import models
from center.models import User
from datetime import datetime
# Create your models here.
class Student(models.Model):
    class Languages(models.TextChoices):
        UZBEK = "uzbek", "O'zbekcha"
        ENGLISH = 'english', "English"
        RUSSIAN = 'russian', "Русский"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User", help_text=("Select User"))
    name = models.CharField(max_length=40, verbose_name=("Student Name"), help_text=("Enter Student Name"), null=True,
                            blank=True)
    phone = models.CharField(max_length=15, unique=True, verbose_name=("Student Phone Number"),
                             help_text=("Enter Student Phone Number"), null=True, blank=True)
    parent = models.CharField(max_length=15, verbose_name=("Parent Phone Number"),
                              help_text=("Enter Parent Phone Number"), null=True, blank=True)
    birth = models.DateField(verbose_name=("Student Birth Year"), help_text=("Enter Student Birth Year"), null=True,
                             blank=True)
    added = models.DateTimeField(auto_now_add=True)
    father_name = models.CharField(max_length=600, null=True, blank=True)
    mother_name = models.CharField(max_length=600, null=True, blank=True)
    language = models.CharField(max_length=15, choices=Languages.choices, verbose_name=("Language"),
                                help_text=("Enter language"), null=True, blank=True)
    address = models.CharField(max_length=100, help_text=("Enter address"), verbose_name=("Address"), null=True,
                               blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    def __str__(self):
        return self.name
class Davomat(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,to_field='phone',related_name='davomat')
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True,unique=True,null=True,blank=True)
    description = models.TextField(default="Sabab ko'rsatilmagan",null=True,blank=True)
    def __str__(self):
        return f"{self.date.strftime('%m/%d/%Y, %H:%M:%S')} vaqtdagi davomat"
    class Meta:
        verbose_name ="Davomat "
        verbose_name_plural ="Davomat "
    