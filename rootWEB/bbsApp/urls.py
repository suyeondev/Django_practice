from django.urls import path
from bbsApp import views

urlpatterns = [
    #http://
    path('main/', views.index, name='main'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('join/', views.join, name='join'),
    # post
    path('bbs_list/', views.list, name='list'),
    path('bbs_registerForm/',views.bbsForm, name='bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name='bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name='bbs_read'),
    path('bbs_remove/', views.bbsRemove, name='bbs_remove'),
    path('bbs_update/',views.bbsUpdate, name='bbs_update'),
    path('bbs_search/',views.bbsSearch, name='bbs_search'),
    path('bbs_reply/',views.bbsReply,name='bbs_reply'),
    path('bbs_line_remove/',views.bbsLineRemove,name='bbs_line_remove'),

    #csv
    path('csvToModel/',views.csvToModel, name='csvToModel'),
    path('upload/',views.upload, name='upload')

]