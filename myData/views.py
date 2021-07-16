from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
import pandas as pd


# Create your views here.
def index(request):
    data = pd.read_csv('myData/static/data/health.csv')
    print(data)
    context = {'csvData': data}
    return render(request, 'viewData.html', context)
    # return HttpResponse('hi')
