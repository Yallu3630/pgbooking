"""PGBooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PGApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('signin/', views.signin),
    path('home/', views.home),
    path('viewRoom/', views.viewRoom),
    path('adminportal/', views.adminportal),
    path('SigninForm/', views.SigninForm),
    path('loginForm/', views.loginForm),
    path('viewUsers/', views.viewUsers),
    path('addRoom/', views.addRoom),
    path('addRoomForm/', views.addRoomForm),
    path('bookingrooms/<int:num>', views.bookingrooms),
    path('bookingForm/', views.bookingForm),
    path('bookedrooms/', views.bookedrooms)
]
