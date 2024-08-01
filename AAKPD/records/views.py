from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.detail import DetailView
from .models import violations
from PIL import Image
from io import BytesIO


def RecordDetailView(request, pk):
    records = violations.objects.get(pk = pk)
    blob = records.photo
    image = Image.open(BytesIO(blob))
    image_bytes = BytesIO()
    image.save(image_bytes, 'JPEG')
    image = image_bytes.getvalue()
    return render(request, 'records/detail.html', {'records': records, 'image': image})

def get_image(request, pk):
    record = violations.objects.get(pk=pk)
    blob = record.photo
    image = Image.open(BytesIO(blob))
    image_bytes = BytesIO()
    image.save(image_bytes, 'JPEG')
    image_data = image_bytes.getvalue()

    response = HttpResponse(image_data, content_type = 'image/jpeg')
    return response

def records_home(request):
    records = violations.objects.order_by('-id')
    return render(request, 'records/records_home.html', {'records': records})


