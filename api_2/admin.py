from django.contrib import admin
from .models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name' , 'employee_roll' , 'employee_city']
