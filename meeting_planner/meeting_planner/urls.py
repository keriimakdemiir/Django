"""
URL configuration for meeting_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from website.views import welcome, about, date

urlpatterns = [
    path('admin/', admin.site.urls),

    # http://127.0.0.1:8000 talebi geldiğinde aşağıda ki url website altıda ki views.py dosyasında bulunan welcome fonksiyonunu tetikleyecek.
    path('', welcome, name='welcome'),

    # http://127.0.0.1:8000/about
    path('about', about),

    # http://127.0.0.1:8000/date
    path('date', date),

    # Meeting App Urls
    path('meetings/', include('meetings.urls'))
]
