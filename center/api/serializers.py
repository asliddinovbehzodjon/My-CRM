from center.models import *
from rest_framework import serializers
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields  = "__all__"
    def create(self, validated_data):
        director = Director.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        return director
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"
    def create(self, validated_data):
        manager = Manager.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        return manager
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields =  "__all__"
    def create(self, validated_data):
        teacher = Teacher.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        return teacher