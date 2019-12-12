"""lotto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

app_name = 'getCron'

urlpatterns = [
    path('', views.index, name='index'),
    path('lottoNumber', views.lotto_number, name='lotto_number'),
    path('getNumber', views.get_number, name='get_number'),
    path('saveNumber', views.save_number, name='save_number'),
    path('listNumber', views.list_number, name='list_number'),
    path('crollingNumber', views.crolling_number, name='crolling_number'),
    path('numberApi', views.numberApi, name='numberApi'),
    # path('getNumber/<int:round_id>/', views.get_number, name='get_number'),
]