from django.db import models
from students.models import Student
from center.models import User
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=150,verbose_name="Course name")
    cost=models.CharField(max_length=100,verbose_name="Course price")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Course '
        verbose_name_plural='Courses '
class Room(models.Model):
    name = models.CharField(max_length=150,verbose_name="Room name")
    student_count = models.CharField(max_length=150, verbose_name="Student Count")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Room '
        verbose_name_plural = 'Rooms '
class Group(models.Model):
    class Education(models.TextChoices):
        ONLINE = 'online', 'Online'
        OFFLINE = 'offline', 'Offline'
    class Day(models.TextChoices):
        juftkunlar = 'juft', 'Juft kunlar'
        OFFLINE = 'toq', 'Toq kunlar'
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        WAITING = 'waiting', 'Waiting'
    name = models.CharField(max_length=100, verbose_name=("Group name"))
    course = models.ManyToManyField(Course, related_name='groups')
    education = models.CharField(max_length=10, choices=Education.choices, null=True, blank=True)
    day = models.CharField(max_length=10, choices=Day.choices, null=True, blank=True)
    student = models.ManyToManyField(Student)
    room = models.ManyToManyField(Room, related_name='groups')
    status = models.CharField(max_length=10, choices=Status.choices, null=True, blank=True)
    start = models.DateField(null=True, blank=True)
    finish = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='myuser')
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Groups"
        verbose_name = " Group "
        verbose_name_plural = " Groups "
