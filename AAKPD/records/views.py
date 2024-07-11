from django.shortcuts import render
from .models import violations

def records_home(request):
    records = violations.objects.all()
    return render(request, 'records/records_home.html', {'records': records})
