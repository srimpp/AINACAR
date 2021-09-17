from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from carinfo.models import Products 
from boards.models import BoardTab as Boards
from members.models import Users

from datetime import datetime
from django.http.response import HttpResponseRedirect


# Create your views here.

def MainFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    
    #-------------------로고 가져오고 난 후 페이징 처리----------------
    logos_all=Products.objects.order_by().values_list('mcar_infoproducts1aker').distinct().order_by('mcar_infoproducts1aker')
    #print(prods) #출력확인
    paginator=Paginator(logos_all, 8) #한번에 8개 출력 
    page=request.GET.get('page', '1')
    try:
        logos=paginator.page(page)
    except EmptyPage:
        logos=paginator.page(paginator.num_pages)
    #------------------------------------------------------------
    
    return render(request, 'main.html',{'logos':logos, 'islogin':request.session['islogin'], 'username':request.session['username']})

def SearchFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    
    #-------------------POST일 경우 검색 실행----------------------------
    if request.method=='POST':
        boardtype=request.POST.get('boardtype')
        searchword=request.POST.get('searchword')
        data_board=None;
        data_carinfo=None;
        #-------------------검색이 전체나 게시판일 경우-----------------------
        if boardtype=='all' or boardtype=='board':
            data_board=Boards.objects.filter(title__icontains=searchword)               | Boards.objects.filter(cont__icontains=searchword)
            data_board=data_board.order_by('-id')
        #-------------------검색이 전체나 차량일 경우-------------------- 
        if boardtype=='all' or boardtype=='carinfo':
            data_carinfo=Products.objects.filter(car_model__icontains=searchword)
    
        return render(request, 'search.html', {'searchword':searchword, 'data_board':data_board, 'data_carinfo':data_carinfo, 'islogin':request.session['islogin'], 'username':request.session['username']})
    
    #--------------------POST가 아닐 경우 메인페이지로 이동--------------------
    else:
        return render(request, 'main.html')
    
def AboutFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    
    return render(request, 'about.html', {'islogin':request.session['islogin'], 'username':request.session['username']})


#현재 세션에 로그인이 되어있는지 확인, 세션이 존재하지 않을 경우 False 부여 (에러방지)
def logincheck(request):
    try: 
        request.session['islogin']
    except KeyError:    
        request.session['islogin']=False
    except Exception as e:
        print("something's wrong", e)
        request.session['islogin']=False
        return render(request, '../members/logout')

