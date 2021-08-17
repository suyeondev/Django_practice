from django.shortcuts import render


def index(request):
    print('rootWEB index~')
    return render(request, 'index.html')