"""midterm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main import views
from django.urls.conf import include
#import members, carinfo, boards, main  - 필요시 사용

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainFunc),
    path('main', views.MainFunc),
    path('search', views.SearchFunc),
    path('about', views.AboutFunc),
    path('members/', include('members.urls')),
    path('carinfo/', include('carinfo.urls')),
    path('boards/', include('boards.urls')),
    
]
