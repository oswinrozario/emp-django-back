from django.urls import path,include
from django.contrib import admin
from . import views
from api_4.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router1 = DefaultRouter()

router1.register('employee_api',views.EmployeeViewSet,
basename='employee')


router2 = DefaultRouter()

router2.register('category_api',views.CategoryViewSet,
basename='category')

urlpatterns = [
    path('',include(router1.urls)),

    path('',include(router2.urls)),

    path('employee_login/', views.employee_login_view, name='login'),

    path('get-token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh-token/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verify-token/',TokenVerifyView.as_view(),name='token_verify'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]

 