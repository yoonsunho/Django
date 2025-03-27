from django.shortcuts import render
from .models import Article

# Create your views here.
# 전체 게시글 조회 후 응답하는 함수
def index(request):
    # 1. db에 전체 게시글 요청
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html',context)       # db와 소통 가능해짐