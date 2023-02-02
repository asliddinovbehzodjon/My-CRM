from rest_framework import serializers
from students.models import *
class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    davomat = DavomatSerializer(many=True,read_only=True)
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields =[
            'user','id'
        ]
        depth=1
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        student = Student.objects.create(**validated_data)
        return student

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields ='__all__'
        