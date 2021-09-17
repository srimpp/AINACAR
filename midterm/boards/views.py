from django.shortcuts import render
from boards.models import BoardTab
from members.models import Users
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.
#게시판 전체목록 출력, GET방식으로 tag가져와서 tag에 해당되는 게시판만 출력하도록 설계 가능

def ListFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    
    #---------------------GET으로 가져온 게시판 타입에 따라 필터---------------------
    btype = request.GET.get('type')      
    if btype=='free':
        datas = BoardTab.objects.filter(type='free').order_by('-gnum', 'onum')
        
    elif btype=='oldcar':
        datas = BoardTab.objects.filter(type='oldcar').order_by('-gnum', 'onum')
        
    elif btype=='travle':
        datas = BoardTab.objects.filter(type='travle').order_by('-gnum', 'onum')
          
    else:
        datas = BoardTab.objects.all().order_by('-gnum', 'onum')
        btype = ''
    
    #페이징 처리
    paginator = Paginator(datas, 10) #한화면에 10행씩출력
    page = request.GET.get('page') #get방식으로 정보를 받아오는 데이터
    try:
        data = paginator.page(page) #page번호를 받아 해당 페이지를 리턴
    except PageNotAnInteger: #들어갔을 때 페이지 번호를 1로
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    #---------------------------------------------------------------
    
    return render(request, 'board.html', {'data':data,'btype':request.GET.get('type'), 'islogin':request.session['islogin'], 'username':request.session['username']})

#새로운 글
#태그 목록: 중고차거래, 자유게시판, 여행
def NewPostFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    return render(request, 'newpost.html', {'islogin':request.session['islogin'], 'username':request.session['username']})

#새 글 확인 (NewPostFunc에 POST처리 조건 추가하는 방법으로 NewPostFunc와 통합 가능)
def NewPostOkFunc(request):
    #POST일 경우 처리
    if request.method == "POST":
        try:
            #group 번호 얻기
            gbun = 1
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('gnum').gnum + 1
                
            BoardTab(
                id=BoardTab.objects.latest('id').id+1,
                name = request.POST.get('name'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0,
                type = request.POST.get('type')
            ).save()
        except Exception as e:
            print('NP 오류 : ', e)
    
    return HttpResponseRedirect('/boards/list')  # 추가 후 목록보기
#내용보기
def ContentFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    
    data = BoardTab.objects.get(id = request.GET.get('id'))
    data.readcnt = data.readcnt + 1     #조회수 증가
    data.save()     #수정
    page = request.GET.get('page')
    return render(request, 'content.html', {'data_one':data, 'page':page, 'islogin':request.session['islogin'], 'username':request.session['username']})

#글/댓글 수정
def UpdatePostFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
    except Exception as e:
        print('UpdateFunc err : ', e)
        
    return render(request, 'update.html', {'data_one':data, 'islogin':request.session['islogin'], 'username':request.session['username']})

#글/댓글 수정 확인 (POST로 인한 통합 가능)
def UpdatePostOkFunc(request):
    upRec = BoardTab.objects.get(id = request.POST.get('id'))
    upRec.name = request.POST.get("name")
    upRec.title = request.POST.get("title")
    upRec.cont = request.POST.get("cont")
    upRec.save()

    return HttpResponseRedirect('/boards/list')      #수정 후 목록보기

#글 삭제
def DeletePostFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
    except Exception as e:
        print('DeleteFunc err : ', e)
    
    return render(request, 'delete.html', {'data_one':data, 'islogin':request.session['islogin'], 'username':request.session['username']})

#글 삭제 확인 (POST로 인한 통합 가능)
def DeletePostOkFunc(request):
    delRec = BoardTab.objects.get(id = request.POST.get("id"))
    userpw=Users.objects.get(username=request.POST.get('username'))
    
    if userpw.password == request.POST.get('del_passwd'):
        delRec.delete()
        return HttpResponseRedirect('/boards/list')  #삭제 후 목록보기
    else:
        return render(request, 'error.html')

#댓글달기
def ReplyFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))     #댓글 대상 원글 읽기
    except Exception as e:
        print('ReplyFunc err : ', e)

    return render(request, 'reply.html', {'data_one':data, 'islogin':request.session['islogin'], 'username':request.session['username']})

#댓글추가 확인 (POST로 인한 통합 가능)
def ReplyOkFunc(request):
    if request.method == 'POST':
        try:
            regnum = int(request.POST.get('gnum'))
            reonum = int(request.POST.get('onum'))
            
            tempRec = BoardTab.objects.get(id = request.POST.get('id')) #원게시글
            old_gnum = tempRec.gnum
            old_onum = tempRec.onum
            
            if old_onum >= reonum and old_gnum == regnum:
                old_onum = old_onum + 1 #onum 갱신 댓글카운트  
            #댓글 저장
            BoardTab(
                id = BoardTab.objects.latest('id').id + 1,
                name = request.POST.get('name'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = regnum,
                onum = old_onum,
                nested = int(request.POST.get('nested')) + 1,
                type = tempRec.type    #원글에서
            ).save()
            
        except Exception as e:
            print('ReplyokFunc err : ', e)
 
    return HttpResponseRedirect('/boards/list')

#글 검색
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
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        #print(s_type, ' ', s_value)
        if s_type == 'title':   #글제목 검색해서 찾기
            datas = BoardTab.objects.filter(title__contains = s_value).order_by('-id')
        elif s_type == 'name':  #작성자 검색해서 찾기
            datas = BoardTab.objects.filter(name__contains = s_value).order_by('-id')
            
        paginator = Paginator(datas, 10) #한화면에 5행씩출력
        page = request.GET.get('page')
        
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
    
        return render(request, 'board.html', {'data':data, 'islogin':request.session['islogin'], 'username':request.session['username']})
    else: 
        if request.GET.get('name'):
            datas=BoardTab.objects.filter(name__contains=request.GET.get('name')).order_by('-id')
            paginator = Paginator(datas, 10) #한화면에 5행씩출력
            page = request.GET.get('page')
            
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)         
            
            return render(request,'board.html', {'data':data, 'islogin':request.session['islogin'], 'username':request.session['username']})
        
        else:
            return HttpResponseRedirect('/boards/list')


def logincheck(request):
    try: 
        request.session['islogin']
    except KeyError:    
        request.session['islogin']=False
    except Exception as e:
        print("something's wrong", e)
        return render(request, '../members/logout')

#DB
#boards: postid title content gnum onum nested +@ tag