from django.http import JsonResponse
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




# select * from bbsuser where user_id = x and user_pwd= x;
# orm : modelName.objects.get()
# select * from bbsuser;
# orm : modelName.objects.all()
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

    return redirect('main')
# post
# SQL : select * from tableName
# ORM : modelName.objects.all()
# list.html -> {% for %} {% endfor %}
def list(request):
    print('bbsApp list~~')
    # model과 연동
    boards = Bbs.objects.all()
    print('boards result:',type(boards), boards)
    context = {'boards': boards,
               'session_user_name'  : request.session['user_name'],
               'session_user_id'    : request.session['user_id']
               }

    return render(request, 'bbs/list.html',context)

def bbsForm(request):
    print('bbsApp bbsForm~')
    context = {
               'session_user_name': request.session['user_name'],
               'session_user_id': request.session['user_id']
               }

    return render(request,'bbs/bbsRegisterForm.html',context)

def bbsRegister(request):
    print('bbs regist~')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        print('bbsApp bbsRegister param:', title, content, writer)

        board = Bbs(title=title, content=content, writer=writer)
        board.save()

        return redirect('list')

def bbsRead(request,id):
    print('bbsRead~~~')
    # model과 작업이 필요
    board=Bbs.objects.get(id=id)
    board.viewcnt = board.viewcnt + 1 # 조회수부분.
    board.save()
    # timeline
    lines=Timeline.objects.filter(board_id=board.id)
    print('board result:',board)

    context = {
        'board':board,
        'session_user_name': request.session['user_name'],
        'session_user_id': request.session['user_id'],
        'lines':lines
    }
    return render(request, 'bbs/read.html',context)

def bbsRemove(request):
    id = request.GET['id']
    print('remove param: ' ,id)
    board = Bbs.objects.get(id=id)
    board.delete()
    return redirect('list')

def bbsUpdate(request):
    id = request.GET['id']
    title=request.GET['title']
    content = request.GET['content']
    board = Bbs.objects.get(id=id)
    board.title=title
    board.content=content
    board.save()
    return redirect('list')

# ajax - json
# title - keyword
# writer - keyword
# select * from tableName where title like '%공지%'
# model.objects.filter(title__icontains='공지')
# select * from tableName where title like '공지%'
# model.objects.filter(title__startswith='공지')
# select * from tableName where title like '%공지'
# model.objects.filter(title__endswith='공지')
def bbsSearch(request):
    print('bbsApp bbsSearch!!')
    type=request.POST['type']
    keyword=request.POST['keyword']
    print('param:',type, keyword)
    if type=='title':
        boards = Bbs.objects.filter(title__icontains=keyword)
    if type== 'writer':
        boards = Bbs.objects.filter(writer__startswith=keyword)
    boardList=[]
    for board in boards:
        boardList.append({
            'id':board.id,
            'title':board.title,
            'writer':board.writer,
            'regdate':board.regdate,
            'viewcnt':board.viewcnt
        })
    return JsonResponse(boardList,safe=False)

def bbsReply(request):
    print('bbsApp bbsReply!')
    time_writer=request.POST['time_writer']
    time_txt=request.POST['time_txt']
    board_id=request.POST['board_id']
    print('param:',time_writer,time_txt,board_id)
    line = Timeline(writer=time_writer,txt=time_txt,board_id=board_id)
    line.save()
    lines= Timeline.objects.filter(board_id = board_id)
    print('lines result', type(lines), lines)
    timeList=[]
    for l in lines:
        timeList.append({
            'id' : l.board_id,
            'writer': l.writer,
            'txt': l.txt
        })

    return JsonResponse(timeList, safe=False)

def bbsLineRemove(request):
    print('bbsApp bbsLineRemove!')
    id = request.POST['id']
    board_id=request.POST['board_id']
    print('param :',id,board_id)
    line = Timeline.objects.get(id=id)
    line.delete()
    lines = Timeline.objects.filter(board_id=board_id)
    print('lines result', type(lines), lines)
    timeList = []
    for l in lines:
        timeList.append({
            'id': l.board_id,
            'writer': l.writer,
            'txt': l.txt
        })

    return JsonResponse(timeList, safe=False)

    # timeline delete
    # timeline filter
    # {{}}
    # jsonResponse()