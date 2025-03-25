import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : '서농'
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html',context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    print(request)  #<WSGIRequest: GET '/catch/?message=ssafy'>
    print(type(request))    # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.GET)      # <QueryDict: {'message': ['ssafy']}>
    print(request.GET.get('message'))   # ssafy
    message = request.GET.get('message')
    context = {
        'message':message,
    }
    return render(request, 'articles/catch.html', context)

def detail(request,num):
    context = {
        'num':num
    }
    return render(request, 'articles/detail.html',context)
    
