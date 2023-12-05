
from django.urls import path
from . import views
urlpatterns = [
    path('student/<int:pk>', views.student_detail ),
    path('students/', views.student_list ),
]
