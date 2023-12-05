from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    student_name = serializers.CharField(max_length=100)
    student_roll = serializers.IntegerField()
    student_city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)