from django.urls import path
from . import views

app_name = 'auth_api'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('generate-otp/', views.GenerateOTPView.as_view(), name='generate-otp'),
    path('verify-otp/', views.VerifyOTPView.as_view(), name='verify-otp'),
    path('login-token/', views.LoginTokenView.as_view(), name='login-token')
]