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
from django.contrib import admin
from django.urls import include, path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import url
# import django.contrib.auth.views

from .views.view import *

urlpatterns = [
    path('myApp/', include('myApp.urls', namespace='myApp')),
    path('lotto/', include('getCron.urls', namespace='getCron')),
    path('funTest/', include('funTest.urls', namespace='funTest')),
    path('myData/', include('myData.urls', namespace='myData')),
    # url(r'^$', myApp.views.index(''), name='index'),
    path('admin/', admin.site.urls),
    path('', index),
    path('test', test),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
