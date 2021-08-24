from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *
# Create your views here.
def index(request):
    print('Poll index!!')
    # model작업
    latest_question_list=QuestionTbl.objects.order_by('regdate')[:5]
    context={'latest_question_list':latest_question_list}

    return render(request,'poll/index.html',context)

def detail(request,id):
    question=get_object_or_404(QuestionTbl,pk=id)
    return render(request,'poll/detail.html',{'question':question})

def vote(request,id):
    question = get_object_or_404(QuestionTbl,pk=id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print('selected_choice:',selected_choice)
    except(KeyError,ChoiceTbl.DoesNotExist):
        return render(request,'poll/detail.html',
                      {'question':question,
                       'error_message':"선택하지 않았습니다.",
                       })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(question.id,)))

def results(request, id):
    question = get_object_or_404(QuestionTbl,pk=id)
    return render(request,'poll/results.html',{'question':question})