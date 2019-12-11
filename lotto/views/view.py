from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


@csrf_exempt #csrf 사용안하기
def test(request):
    return HttpResponse('test')
