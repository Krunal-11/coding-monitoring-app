from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('admin', views.admin_panel, name='admin'),
    path('hod', views.hod_panel, name='hod'),
    path('validate', views.validate, name='router'),
    path('students', views.display_students, name='r21'),
    path('update', views.update, name='update'),

]
