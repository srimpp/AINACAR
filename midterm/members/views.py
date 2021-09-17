from django.shortcuts import render, redirect
from members.models import Users
from django.http.response import HttpResponseRedirect, HttpResponse

#로그인 페이지로 이동, 기본
def LoginPageFunc(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    #로그인 정보 받고 세션 생성
    elif request.method =='POST':
        try:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            login_data = {} # 딕트타입으로 정보 담고 웹에 출력
            if not (username and password): # 아이디 비밀번호 입력 안할 시에
                login_data['error'] = '아이디와 비밀번호를 입력해주세요' # login_data 세션 키에 error값 저장 

            else:
                user = Users.objects.get(username=username) # 입력한 값 아이디 받고 

                if user != None: # 아이디가 있으면 
                    if password == user.password: # 비밀번호 일치하면 로그인 
                        #-------------------------------------REQUEST 생성--------------------------------------------------
                        request.session['islogin']=True #로그인이 켜짐
                        request.session['user'] = user.id # user 세션 key에 로그인한 user의 아이디 값 저장
                        request.session['username']=user.username
                        request.session.set_expiry(7200)
                        #-------------------------------------REQUEST 생성 끝---------------------------------------------
                        return redirect('/members/login')

                    else:
                        login_data['error'] = '비밀번호를 다시 입력하세요'

            return render(request, 'login.html', login_data)

        except Exception as e: #아이디가 없으면 
            login_data['error'] = '해당 아이디가 없습니다 회원가입 해주세요'
            #print('에러메세지 : ',e)
            return render(request, 'login.html', login_data)
            
#로그인 성공시 테스트페이지
def LoginFunc(request):
    return redirect('/')

#로그아웃하기, 이전 페이지(혹은 메인 페이지)로 Redirect
def LogOutFunc(request):
    if request.session['user']:
        #del request.session['user']
        request.session.clear()
    return redirect('/') # 메인으로



#회원가입
#ID, 비번, 이름, 전화번호, 이메일, 가입날짜 

def NewMemFunc(request):
    if request.method == 'GET':
        return render(request, 'newmember.html')
    elif request.method == 'POST':
        Users(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
            full_name = request.POST.get('full_name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
        ).save()
        
        return HttpResponseRedirect('/members/main')
    else:
        return render(request, 'error.html')

# 아이디 확인용
def IdChkFunc(request):
    try:
        username = request.GET.get('username')
        isRegi = False
        
        datas = Users.objects.get(username=username) 
        
        if datas != None:
            isRegi = True
    except Exception as err:
        print('err', err)
    
    return render(request, 'idcheck.html', {'username':isRegi})
    

#전체 회원 목록 출력
#admin 회원을 먼저 만들어서 admin으로 로그인 했을때만 접속 가능하도록 설계 가능
def ListMemFunc(request):
    lists = Users.objects.all()
    return render(request, 'members.html', {'members':lists})


# 내 계정 보기
def AccountFunc(request):
    if request.method == 'GET':
        user=""
        currentid=request.session['user']
        try:
            user = Users.objects.get(id=currentid)
            #print(user)
        except Exception as e:
            print("AccountFunc err: ", e)
    
        return render(request, 'mypage.html', {'user_one':user})
    
    if request.method == 'POST':
        try:
            user_id = request.session['user']
            if user_id:
                update_user = Users.objects.get(id = request.POST.get('id'))
                if  update_user.password == request.POST.get('up_passwd'):
                    update_user.email = request.POST.get('email')
                    update_user.phone = request.POST.get('phone')
                    update_user.save()
                return HttpResponseRedirect('/members/login')
            
            else:
                return render(request, 'error.html')
        
        except Exception as e:
            print('AccountFunc err: ',e)

            
def logincheck(request):
    try: 
        request.session['islogin']
    except KeyError:    
        request.session['islogin']=False
    except Exception as e:
        print("something's wrong", e)
        request.session['islogin']=False
        return render(request, '../members/logout')            

