from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def about(request):
    data = {
        'title': 'Про нас',
        'values': ['Some', 'Hello', 'World!!']
    }
    return render(request, 'main/about.html', data)

def example(request):
    return render(request, 'main/example.html')

 