from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import violations
import base64

class ImageView(View):
    def get(self, request, image_id):
        try:
            image = violations.objects.get(pk=1)
            
            # Получаем изображение в виде base64-строки
            image_data = image.get_image_as_base64()
            # Отправляем изображение в браузер
            response = HttpResponse(image_data, content_type='image/jpeg')
            return response
        except violations.DoesNotExist:
            return HttpResponse('Image not found', status=404)

def records_home(request):
    records = violations.objects.order_by('-id')
    return render(request, 'records/records_home.html', {'records': records})

def record(request):
    record = violations.objects.order_by('-id')[:1]
    
    return render(request, 'records/record.html', {'record': record})
