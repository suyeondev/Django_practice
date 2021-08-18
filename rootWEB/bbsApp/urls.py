from django.urls import path
from bbsApp import views

urlpatterns = [
    #http://
    path('main/', views.index, name='main'),
    path('bbs_list/', views.list, name='list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('join/', views.join, name='join'),

]