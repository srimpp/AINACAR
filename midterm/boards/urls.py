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
from boards import views
#from main import views
#from django.urls.conf import include
#import members, carinfo, boards, main  - 필요시 사용

urlpatterns = [
    path('',views.ListFunc),
    #1. 게시판 보기 (기본), ListFunc로 이동
    path('list', views.ListFunc),
    #2. 게시판 만들기, NewPostFunc로 이동
    path('newpost', views.NewPostFunc),
    #3. 게시판 등록하기, NewPostOkFunc로 이동
    path('newpostok', views.NewPostOkFunc),
    #4. 게시판 내용보기 ContentFunc로 이동
    path('content', views.ContentFunc),
    #5. 게시판 수정 UpdatePostFunc로 이동
    path('updatepost', views.UpdatePostFunc),
    #6. 게시판 수정 확인 UpdatePostOkFunc로 이동
    path('updatepostok', views.UpdatePostOkFunc),
    #7. 게시판 삭제, DeletePostFunc로 이동
    path('deletepost', views.DeletePostFunc),
    #8. 게시판 삭제확인
    path('deletepostok', views.DeletePostOkFunc),
    #8. 게시판 검색
    path('search', views.SearchFunc),
    #9. 댓글 쓰기, ReplyFunc로 이동
    path('reply', views.ReplyFunc),
    #10. 댓글 올리기, ReplyOkFunc로 이동
    path('replyok', views.ReplyOkFunc)
    
]
