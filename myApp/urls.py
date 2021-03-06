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
from django.urls import path, re_path
from django.conf.urls import url
from .views.view import *
from .views.hi import *

app_name = 'myApp'

urlpatterns = [
    path('hi', say_hi),
    path('form', inputForm),
    path('', index, name='index'),
    path('html', index_html, name='index_html'),
    path('html/parent', parent, name='parent'),
    path('html/<int:question_id>/', detail, name='detail'),
    path('html/<int:question_id>/vote/', vote, name='vote'),
    path('html/<int:question_id>/results/', results, name='results'),
]
