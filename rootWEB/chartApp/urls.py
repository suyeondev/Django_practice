from django.urls import path, include
from chartApp import views

urlpatterns = [
    path('main/', views.index),
    path('line/', views.line),
    path('bar/', views.bar),
    path('wordcloud/', views.wordcloud),
]
