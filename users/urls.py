from django.urls import path
from . import views

urlpatterns = [
    path('change_pwd/', views.change_pwd_method, name = 'change_pwd'), 
    path('civilian/', views.civilian_method, name = 'civilian'), 
    path('civilian_edit/', views.edit_c_method, name = 'edit_c'), 
    path('civilian_test/', views.test_c_method, name = 'test_c'), 
    path('officer/', views.officer_method, name = 'officer')
]
