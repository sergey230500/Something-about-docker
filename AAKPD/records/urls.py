from django.urls import path
from . import views

urlpatterns = [
    path('', views.records_home, name='records_home'),
    path('record', views.record, name='record'),

]
