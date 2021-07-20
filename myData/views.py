from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
import pandas as pd


# Create your views here.
def index(request):
    data = pd.read_csv('myData/static/data/health.csv')
    # print(data['수면시간'].value_counts())
    print(data.dtypes)
    context = {'csvData': data['심박수']}
    return render(request, 'mydata/data_view.html', context)
    # return HttpResponse('hi')
