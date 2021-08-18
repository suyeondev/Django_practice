from django.shortcuts import render, redirect

from .models import *

# Create your views here.
def index(request):
    print('bbsApp index~~')
    #세션 유무를 체크하는 로직이 필요하다.
    if request.session.get('user_name'):
        print('session exist~~')
        context={
            'session_user_name' : request.session['user_name'],
            'session_user_id' : request.session['user_id']
        }
        return render(request, 'bbs/home.html',context)
    return render(request, 'bbs/login.html')

def list(request):
    print('bbsApp list~~')
    return render(request, 'bbs/list.html')


# select * from bbsuser where user_id = x and user_pwd= x;
# orm : modelName.object.get()
# select * from bbsuser;
# orm : modelName.object.all()
def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['pwd']
        user = BbsUser.objects.get(user_id = id, user_pwd = pwd)
        print('user result:', user)
        context = {}
        if user is not None :
            # 세션을 만드는 과정
            request.session['user_name'] = user.user_name;
            request.session['user_id'] = user.user_id;
            # 세션을 심는 과정 - 모든 데이터를 담는게 X, 세션마다 유지되어야 하는 것만 담기.
            context['session_user_name'] = request.session['user_name']
            context['session_user_id'] = request.session['user_id']

    return render(request, 'bbs/home.html',context)

def logout(request):
    print('bbsApp logout~~~~~')
    request.session['user_name'] = {};
    request.session['user_id'] = {};
    request.session.modified =True

    return redirect('main')

def registerForm(request):
    print('bbsApp registerForm~~')
    return render(request,'bbs/join.html')

def join(request):
    print('bbsApp join~~~')
    if request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['pwd']
        name = request.POST['name']

        BbsUser(user_id=id, user_pwd=pwd, user_name = name).save()
        print('user result:', join)
    return redirect('main')
