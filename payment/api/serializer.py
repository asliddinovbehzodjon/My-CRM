from rest_framework.serializers import  ModelSerializer
from rest_framework  import serializers
from payment.models import StudentPayment
class StudentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPayment
        fields = "__all__"
