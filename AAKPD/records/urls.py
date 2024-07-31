from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.records_home, name='records_home'),
    path('<int:pk>/', views.RecordDetailView.as_view(), name='detail'),
    path('<int:pk>/image', views.get_image, name = 'image')

]
