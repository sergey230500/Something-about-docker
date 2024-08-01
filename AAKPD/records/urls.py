from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.records_home, name='records'),
    path('<int:pk>/', views.RecordDetailView, name='detail'),
    path('<int:pk>/image', views.get_image, name = 'image')

]
