from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


# Create your views here.
def index(request):
    data = pd.read_csv('myData/static/data/health.csv')
    # print(data['수면시간'].value_counts())
    print(data.dtypes)
    context = {'csvData': data['심박수']}
    return render(request, 'mydata/data_view.html', context)
    # return HttpResponse('hi')


def static(request):
    titanic = sns.load_dataset('titanic')
    em_pie = titanic['embarked'].value_counts()
    em_pie.plot(kind='pie', autopct='%1.1f%%', figsize=(10,6)) # 원그래프
    sns.countplot(data=titanic, x='embarked') # 막대그래프

    return HttpResponse("Hello")
