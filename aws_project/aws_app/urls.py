from django.urls import path
from aws_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
]