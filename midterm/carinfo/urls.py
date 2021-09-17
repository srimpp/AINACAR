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
from carinfo import views
#from main import views
#from django.urls.conf import include
#import members, carinfo, boards, main  - 필요시 사용


urlpatterns = [
    #1. 기본은 ListBrandFunc로 이동
    path('', views.ListBrandFunc),
    #2. product: 특정 상품 출력, ProductFunc로 이동
    path('product', views.ProductFunc),
    #3. 댓글 쓰기, ReplyFunc로 이동
    path('postcomment', views.CommentFunc),
]
