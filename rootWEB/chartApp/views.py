from django.shortcuts import render

# Create your views here.

def index(request):
    print('chartApp index~~~')
    return render(request, 'chart/index.html')

def line(request):
    print('chartApp line~~')
    seoul=[15.0, 6.9, 9.5, 14.5, 18.2, 29.5, 25.2, 23.3, 18.3, 13.9, 9.6]
    london=[ 10.9, 4.2, 5.7, 8.5, 11.9, 9.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
    context ={
        'seoul' : seoul,
        'london': london
    }
    return render(request, 'chart/line.html',context)

def bar(request):
    print('chartApp bar~~')
    Year1800=[107, 31, 635, 203, 20]
    Year1900=[133, 156, 947, 408, 6]
    Year2000=[814, 841, 3714, 727, 31]
    Year2016=[1216, 1001, 4436, 738, 40]
    context = {
        'Year1800': Year1800,
        'Year1900': Year1900,
        'Year2000': Year2000,
        'Year2016': Year2016
    }
    return render(request, 'chart/bar.html',context)

def wordcloud(request):
    print('chartApp wordcloud~~')

    return render(request, 'chart/wordcloud.html')