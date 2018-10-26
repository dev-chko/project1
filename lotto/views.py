from django.shortcuts import render, redirect

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
    key = request.GET['lotto_num']
    GuessNumbers.objects.get(id=key)
    return render(request,'lotto/detail.html', {'lotto':lotto})

def detail2(request, num):
    lotto = GuessNumbers.objects.get(id=num)
    print(lotto)
    return render(request, 'lotto/detail2.html', {'lotto':lotto})