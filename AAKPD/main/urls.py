from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('about', views.about, name='about'),
    path('example', views.example)
]
