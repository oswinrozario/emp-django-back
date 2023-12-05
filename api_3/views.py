from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_api(request):
    if(request.method == 'GET'):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    if(request.method == 'POST'):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return(Response({'msg':'data created'}))
        return Response(serializer.errors)
    
    if(request.method == 'PUT'):
        id = request.data.get('id')
        emp = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(emp,data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)
    
    if(request.method == 'DELETE'):
        id = request.data.get('id')
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return Response({"msg":"deleted"})
        