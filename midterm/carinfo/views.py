from django.shortcuts import render
from carinfo.models import Products, CarinfoComments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.

#전체 상품 목록 출력
#특정 브랜드를 클릭하면 해당 브랜드 상품 목록만 출력
#GET 방식으로 필터해서 지정된 브랜드 상품만 출력, 또는 브랜드별 페이지 작성
def ListBrandFunc(request):
    #-------------------SESSION CHECK------------------------------
    #checking login status
    logincheck(request)
    #print(request.session['islogin'])
    try:
        request.session['username']
    except KeyError:
        request.session['username']=''
    #-------------------SESSION CHECK END------------------------------
    
    #---------------------데이터 반환/필터------------------------------
    datas = Products.objects.all() # 전체 브랜드 가져오기
    brand='all' 
    if request.GET.get("brand"): # 주소창을 통해 브랜드 정보 get방식으로 가져올 수 있다면
        if request.GET.get("brand")!='all': # 브랜드가 전체가 아니라면
            brand=request.GET.get('brand') # URL의 브랜드 정보를 'brand'객체에 치환
            datas = datas.filter(mcar_infoproducts1aker=request.GET.get("brand")) # 해당 브랜드 메이커 데이터만 새로 담는다.
    #print(brand) # 출력 확인용       

    if request.GET.get("rdate")=='True': # 출시일 데이터 가져오기(T=오름차순, F=내림차순)
        #print(request.GET.get('brand'))
        datas = datas.order_by('-rdate') # 오름차순
    elif request.GET.get("rdate")=='False':
        datas = datas.order_by('rdate') # 내림차순
    #---------------------------------------------------------------
    
    
    #--------------------로고 페이징 작업------------------------------
    logos_all=Products.objects.order_by().values_list('mcar_infoproducts1aker').distinct() # 중복을 제거한 메이커 목록
    
    paginator=Paginator(logos_all, 14) # 브랜드 로고출력(페이지당 14개 출력)
    page=request.GET.get('page', '1') # 페이지 데이터를 가져오면서 항상 1페이지로 초기화
    
    try:
        logos=paginator.page(page)
    except EmptyPage:
        logos=paginator.page(paginator.num_pages)
    # 여기까지 로고 페이징 작업
    #---------------------------------------------------------------
    
    
    #---------------------차량목록 페이징------------------------------------------
    paginator2 = Paginator(datas, 10) # 차량모델 출력(페이지당 10개 출력)
    
    page2 = request.GET.get('page2', '1')
    #print(page2) # 현재 페이지 출력(웹에서 받아온 페이지 번호)
    try:
        datas = paginator2.page(page2)
    except PageNotAnInteger:
        datas = paginator2.page(1)
    except EmptyPage:
        datas = paginator2.page(paginator2.num_pages)
         
    # print(datas) # 페이지 수 확인
    # print("allpage", allpage)

    allpage = range(paginator2.num_pages + 1) # 페이지는 파이썬 특성상 0부터 시작하기 때문에 전체 +1
    #------------------------------------------------------------------------------------
    
    
    return render(request, 'brands.html', {'pro':datas, 'logos':logos, 'allpage':allpage, 'brand':brand, 'islogin':request.session['islogin'], 'username':request.session['username']})
    
    

#개별 상품 정보 출력
#GET 방식 사용가능
def ProductFunc(request):
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
        #---------------------상품 데이터 반환------------------------------------------
        # infos = Products.objects.get(id = request.GET['id'])
        # print(infos)
        if request.GET.get('id'): # URL로부터 id값을 받아온다.
            datas = Products.objects.filter(id = request.GET['id']) # id와 일치하는 자료를 필터링해준다.
            # print(datas)
        
            logos_all = Products.objects.order_by().values_list('mcar_infoproducts1aker').distinct()
            # 차량의 제조사의 중복 데이터를 없애주고 각 차량 메이커의 브랜드 로고를 가져올 수 있도록 자료를 뽑아준다.
            
            #상응하는 댓글 목록 반환, 날짜로 정렬
            allcomments=CarinfoComments.objects.filter(carid=request.GET['id']).order_by('rdate')
        
        return render(request, 'product.html', {'pro':datas, 'logos':logos_all, 'allcomments':allcomments, 'islogin':request.session['islogin'], 'username':request.session['username']})
        

    except Exception as e:
        print('잘못된 접근입니다, 에러: ', e)
    return HttpResponseRedirect('/carinfo')

#댓글 기능 
#POST로 들어올 경우에만 처리, 외엔 원글로 돌아감
def CommentFunc(request):
    if request.method=='POST':
        try:
            #print(request.POST.get('carid'))
            #print(request.POST.get('username'))
            #print(request.POST.get('comment'))
            #print(CarinfoComments.objects.latest('id').id)
            CarinfoComments(
                id=CarinfoComments.objects.latest('id').id + 1,
                carid=request.POST.get('carid'),
                username = request.POST.get('username'),
                comments = request.POST.get('comment'),
                rdate = datetime.now(),
            ).save()
        except Exception as e:
            print('오류 : ', e)
    return HttpResponseRedirect("/carinfo/product?id="+request.POST.get('carid'))


#세션확인
def logincheck(request):
    try: 
        request.session['islogin']
    except KeyError:    
        request.session['islogin']=False
    except Exception as e:
        print("something's wrong", e)
        request.session['islogin']=False
        return render(request, '../members/logout')

#DB
#1. Products: 자동차 정보 DB
#2. carinfo_comments: 게시글id, 차량모델(FK), username(FK), comment, rdate