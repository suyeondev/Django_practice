from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('fromApp index~~')
    return render(request, 'front/index.html')

def scriptIndex(request) :
     print('frontApp scriptIndex~~')
     return render(request, "front/script.html")
# ajax 통신방식
def idChkAjax(request) :
    print('frontApp idChkAjax~~~')
    id = request.POST['id']
    print('param ~ ' , id)
    list = [{'msg' : '확인'}]
    return JsonResponse(list , safe=False)

def staticFun(request):
    print('frontApp StaticFunc~~')
    return render(request, 'front/static_page.html')

def navFun(request):
    print('frontApp navFunc~')
    return render(request, 'front/navbar.html')

def bootFun(request):
    print('frontApp bootFun~~')
    return render(request, 'front/boot_page.html')