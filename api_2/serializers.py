from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    employee_name = serializers.CharField(max_length=100)
    employee_roll = serializers.IntegerField()
    employee_city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.employee_name = validated_data.get('employee_name', instance.employee_name)
        instance.employee_roll = validated_data.get('employee_roll', instance.employee_roll)
        instance.employee_city = validated_data.get('employee_city', instance.employee_city)
        instance.save()
        return instance