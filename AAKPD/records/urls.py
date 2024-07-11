from django.urls import path
from . import views

urlpatterns = [
    path('records_home', views.records_home, name='records_home'),

]
