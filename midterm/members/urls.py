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
from members import views
#from main import views
#from django.urls.conf import include
#import members, carinfo, boards, main  - 필요시 사용


urlpatterns = [
    # 세션 
    path('', views.LoginFunc),

    # members 안 기본값은 LoginPageFunc로 이동
    path('main', views.LoginPageFunc),
    
    # LoginFunc: 로그인, LoginFunc로 이동
    path('login', views.LoginFunc),
    
    #logout: 로그아웃, LogOutFunc로 이동
    path('logout', views.LogOutFunc),

    # newmember: 회원가입, NewMemFunc로 이동
    path('newmember', views.NewMemFunc),
    
    # idcheck : 아이디 확인용 IdChkFunc로 이동
    path('idcheck', views.IdChkFunc), 
    
    # 내계정 
    path('account', views.AccountFunc), 
    
    # allmembers: 회원목록 출력, ListMemFunc로 이동
    path('allmembers', views.ListMemFunc),
]
