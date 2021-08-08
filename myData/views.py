from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.conf import settings
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import savefig

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


def solution(a):
    return ''.join(a.split(','))


def dataSet(request):
    data = pd.read_csv('myData/static/data/Seoul_Park.csv')

    columns = ['유료합계', '어른', '청소년', '어린이', '외국인', '단체', '무료합계', '총계']

    # 숫자에 콤마 제거
    for i in columns:
        data[i] = data[i].apply(lambda e: solution(e))

    # int형으로 변경 - 에러일때는 0
    for i in columns:
        data[i] = pd.to_numeric(data[i], errors='coerce').fillna(0)

    #날짜포멧
    data['날짜'] = pd.to_datetime(data['날짜'])
    print(data.dtypes)
    data['연'] = data['날짜'].dt.year
    data['월'] = data['날짜'].dt.month
    data['일'] = data['날짜'].dt.day
    data['요일(num)'] = data['날짜'].dt.dayofweek

    print(data.head())

    context = {'csvData': data}
    return render(request, 'mydata/data_view.html', context)


def staticGraph(request):
    static_root = "static/image/"
    titanic = sns.load_dataset('titanic')
    em_pie = titanic['embarked'].value_counts()
    circleGraph = em_pie.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6))  # 원그래프
    plt.savefig(static_root + "circle.png")
    plt.clf()

    stickGraph = sns.countplot(data=titanic, x='embarked')  # 막대그래프
    plt.savefig(static_root + "stick.png")
    plt.clf()

    join1 = sns.jointplot(x="age", y="fare", data=titanic)
    join1.savefig(static_root + "join1.png")
    plt.clf()

    join2 = sns.jointplot(x="age", y="fare", data=titanic, kind="kde")
    join2.savefig(static_root + "join2.png")
    plt.clf()

    sns.boxplot(data=titanic, x='sex', y='age', hue='class')
    plt.savefig(static_root + "boxplot.png")
    plt.clf()
    # 복수그래프
    g = sns.FacetGrid(data=titanic, col='sex', row='survived')
    g.map(plt.hist, 'age')
    plt.savefig(static_root + "FacetGrid.png")
    plt.clf()

    # 복수그래프
    # g.map(plt.scatter, 'age', 'fare')
    # plt.savefig(static_root + "FacetGrid2.png")
    # plt.clf()

    # 히스토그램/커널밀도 그래프
    sns.distplot(titanic['fare'])
    plt.savefig(static_root + "histKde.png")
    plt.clf()

    # 데이터 간 상관관계
    print(titanic.corr())

    # 히트맵
    sns.heatmap(titanic.corr())
    plt.savefig(static_root + "hitmap.png")
    plt.clf()

    # 정규분포
    titanic['fare_log'] = np.log1p(titanic['fare'])
    sns.distplot(titanic['fare_log'])
    np.expm1(titanic['fare_log'].describe())  # 데이터 지수화 처리
    plt.savefig(static_root + "fareLog.png")
    plt.clf()

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

        if (data.Index > 10):
            break

    context = {
        'staticData': dataSet
        , "baseImgUrl": "/" + static_root
        , "stickImgUrl": "stick.png"
        , "circleImgUrl": "circle.png"
        , "joinImgUrl": "join1.png"
        , "join2ImgUrl": "join2.png"
        , "boxImgUrl": "boxplot.png"
        , "faceImgUrl": "FacetGrid.png"
        , "histKdeImgUrl": "histKde.png"
        , "hitmapImgUrl": "hitmap.png"
        , "fareLogImgUrl": "fareLog.png"
    }

    return render(request, 'mydata/static_view.html', context)
