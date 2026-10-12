from django.urls import path
from aws_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('view_data/', views.view_data, name="view_data"),
]