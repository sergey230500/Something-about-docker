from django.urls import path
from . import views
from .views import ImageView

urlpatterns = [
    path('image/<int:image_id>/', ImageView.as_view(), name='image'),
    path('', views.records_home, name='records_home'),
    path('record', views.record, name='record'),

]
