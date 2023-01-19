from django.urls import path,include
from center.api.views import *
from students.api.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('director',DirectorViewset)
router.register('manager',ManagerViewset)
router.register('teacher',TeacherViewset)
router.register('students',StudentViewset)
urlpatterns  = [
    path('',include(router.urls))
]