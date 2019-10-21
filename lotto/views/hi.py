from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader


def say_hi(request):
    return render(request, 'default/hi.html', {'name':'jiji'})


def inputForm(request):
    return render(request, 'default/input.html')


def rp(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def process(request):
    if request.method == 'GET':
        id = request.GET['id']
    elif request.method == 'POST':
        id = request.POST['id']

    text = 'method : '+request.method+'<br>'
    text += 'my id : '+id
    return HttpResponse(text)