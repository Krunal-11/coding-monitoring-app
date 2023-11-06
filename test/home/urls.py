from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('customlogin', views.custom_login, name='customlogin'),
    path('adminpanel', views.admin_panel, name='admin_panel'),
    path('hod', views.hod_panel, name='hod_panel'),
    path('validate', views.validate, name='router'),
    path('students', views.display_students, name='r21'),
    path('update', views.update, name='update'),

]
