from django.urls import path
from . import views

urlpatterns = [
    path('forgot/', views.forgot_method, name = 'forgot'), 
    path('login_civilian/', views.login_method_c, name = 'login_c'), 
    path('login_officer/', views.login_method_o, name = 'login_o'), 
    path('logout/', views.logout_method, name = 'logout'), 
    path('otp/', views.otp_method, name = 'otp'), 
    path('respond/', views.respond_method, name = 'respond'), 
    path('signup_civilian/', views.signup_method_c, name = 'signup_c'), 
    path('signup_officer/', views.signup_method_o, name = 'signup_o')
]
