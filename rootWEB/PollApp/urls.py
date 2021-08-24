from PollApp import views
from django.urls import path

urlpatterns = [
    path('main/',views.index, name='main'),
    path('main/<int:id>/',views.detail, name='detail'),
    path('main/<int:id>/vote',views.vote, name='vote'),
    path('main/<int:id>/results',views.results, name='results'),


]
