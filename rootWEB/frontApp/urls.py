from django.urls import path
from frontApp import views

urlpatterns = [
    path('main/',views.index),
    path('script_page/',views.scriptIndex),
    path('idChkAjax/',   views.idChkAjax),
    path('static/',views.staticFun ),
    path('navbar/',views.navFun),
    path('bootstrap/', views.bootFun),

]
