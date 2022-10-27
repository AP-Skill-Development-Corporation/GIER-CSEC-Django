"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from SampleApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/',views.demo),
    path('p/',views.sample),
    path('w/<str:aq>/',views.hrf),
    path('g/<str:r>/<int:y>/<str:k>/',views.stdnt),
    path('k/',views.wg),
    path('y/<str:qw>/',views.dgh),
    path('h/<str:nm>/',views.ae),
    path('ty/',views.jy),
    path('nu/<str:k>/',views.cy),
    path('yu/',views.gk),
    path('ju/<str:qy>/',views.vy),
    path('rg/',views.std),
    path('rb/',views.me),
]




