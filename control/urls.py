# control/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ligar/', views.ligar, name='ligar'),
    path('desligar/', views.desligar, name='desligar'),
    path('aumentar/', views.aumentar, name='aumentar'),
    path('diminuir/', views.diminuir, name='diminuir'),
    path('definir-temperatura/', views.definir_temperatura, name='definir_temperatura'),
]
