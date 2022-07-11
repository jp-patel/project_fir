"""project_fir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name = 'home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name = 'home')
Including another URLconf
    1. Import the include() function:from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_method, name = 'index'), 
    path('about/', views.about_method, name = 'about'), 
    path('admin/', admin.site.urls), 
    path('contact_us/', views.contact_method, name = 'contact'), 
    path('documantation/', views.docs_method, name = 'docs'), 
    path('fir/', include('fir.urls')), 
    path('privacy/', views.privacy_method, name = 'privacy'), 
    path('redirect/', include('login.urls')), 
    path('resources/', views.resources_method, name = 'resources'), 
    path('tac/', views.tac_method, name = 'tac'), 
    path('test/', views.test_method, name = 'test'), 
    path('user/', include('users.urls'))
]
