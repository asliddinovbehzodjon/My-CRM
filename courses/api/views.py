from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import *
from courses.models import *
# Create your views here.
class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
class RoomViewset(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
class GroupsViewset(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        group = Group.objects.create(name=data['name'], education=data.get('education', None),
                                      status=data.get('status', None), start=data.get('start', None),
                              finish=data.get('finish', None), user=request.user)
        group.save()
        if 'rooms' in data:
            for room in data['room']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'courses' in data:
            for course in data['course']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'students' in data:
            for student in data['students']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group.student.add(xona)
                except Student.DoesNotExist:
                    pass

        serializer = GroupSerializer(group)
        return Response(serializer.data)


    def partial_update(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'rooms' in data:
            for room in data['rooms']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.add(xona)
                except Room.DoesNotExist:
                    pass
        if 'courses' in data:
            for course in data['courses']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.add(xona)
                except Course.DoesNotExist:
                    pass
        if 'students' in data:
            for student in data['students']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group_object.education = data.get('education', group_object.education)
        group_object.status = data.get('status', group_object.status)
        group_object.start = data.get('start', group_object.start)
        group_object.finish = data.get('finish', group_object.finish)
        group_object.user = data.get(request.user, group_object.user)
        serializer = GroupSerializer(group_object)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'room' in data:
            for room in data['rooms']:
                try:
                    xona = Room.objects.get(id=room['id'])
                    group_object.room.remove(xona)
                except Room.DoesNotExist:
                    pass
        if 'courses' in data:
            for course in data['courses']:
                try:
                    xona = Course.objects.get(id=course['id'])
                    group_object.course.remove(xona)
                except Course.DoesNotExist:
                    pass
        if 'students' in data:
            for student in data['students']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.remove(xona)
                except Student.DoesNotExist:
                    pass

        serializer = GroupSerializer(group_object)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        return self.partial_update(request)