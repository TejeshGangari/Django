from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name='Home Page'),
    path('add', views.add, name='add')

]