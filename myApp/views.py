from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'myApp/index.html')
#     return HttpResponse("Hello, world. You're at the polls index.")
