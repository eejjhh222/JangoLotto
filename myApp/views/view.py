from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the myApp/view index.")


def index_html(request):
    return render(request, 'myApp/index.html')


def detail(request):
    return render(request, 'myApp/index.html')
