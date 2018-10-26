from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from lotto.form import PostForm
from .models import *

def index(request):
    lottos = GuessNumbers.objects.all()
    location = Location.objects.get(id=1)
    return render(request, 'lotto/index.html', {'lottos':lottos, 'location': location})

def post(request):
    if request.method =="GET":
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})
    else:
        form = PostForm(request.Post)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('/lotto')

def detail(request):
    key = request.GET['lotto_number']
    lotto = GuessNumbers.objects.get(id=key)
    return render(request,'lotto/detail.html', {'lotto':lotto})

def detail2(request, num):
    lotto = GuessNumbers.objects.get(id=num)
    print(lotto)
    return render(request, 'lotto/detail.html', {'lotto':lotto})

def join(request):
    if request.method == 'GET':
        return render(request,'lotto/join.html',{})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']
        #실제 회원가입 - Member에 테이블 데이터 입력
        m = Member(id=id, pw=pw, name=name)
        m.save()
        return render(request, 'lotto/join_result.html', {'id':id, 'name':name})
@csrf_exempt
def id_check(request):
    id = request.POST['id']
    try:
        Member.objects.get(id=id)
    except Member.DoesNotExist as e:
        pass
        return HttpResponse('가입가능')
    else:
        return HttpResponse('가입불가')