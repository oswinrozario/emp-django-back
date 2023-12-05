from . import views
from django.urls import path

urlpatterns = [
    path('employees/',views.employee_api),
]