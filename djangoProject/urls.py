"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import LongitudeLatitude
from gameapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', TemplateView.as_view(template_name = 'login.html')),
    path('login/', views.login, name="login"),
    path('longitude/', ListView.as_view(model=LongitudeLatitude, template_name="longitude.html")),
    path('list/', views.list),
    path('apply/', views.apply, name="apply"),
]
