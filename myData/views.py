from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

import matplotlib.pyplot as plt
import warnings
import numpy as np
import seaborn as sns
import pandas as pd


# Create your views here.
def index(request):
    data = pd.read_csv('myData/static/data/health.csv')
    # print(data['수면시간'].value_counts())
    print(data.dtypes)
    context = {'csvData': data['심박수']}
    return render(request, 'mydata/data_view.html', context)
    # return HttpResponse('hi')


def static(request):
    static_root = "static/image/"
    titanic = sns.load_dataset('titanic')
    em_pie = titanic['embarked'].value_counts()
    em_pie.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6))  # 원그래프
    sns.countplot(data=titanic, x='embarked')  # 막대그래프

    # join1 = sns.jointplot(x="age", y="fare", data=titanic)
    # join1.savefig(static_root + "join1.png")
    # join2 = sns.jointplot(x="age", y="fare", data=titanic, kind="kde")
    # join2.savefig(static_root + "join2.png")
    # plt.clf()
    dataSet = [];
    for data in titanic.itertuples():
        dataSet.insert(data.Index, {
            "survived": data.survived,
            "sex": data.sex,
            "age": data.age,
            "sibsp": data.sibsp,
            "embarked": data.embarked,
            "who": data.who,
            "alive": data.alive,
            "alone": data.alone
        })

        if(data.Index > 10) :
            break

    context = {'staticData': dataSet}
    return render(request, 'mydata/static_view.html', context)
