from django.shortcuts import render,redirect  # 여기 추가 해줘야함
from .models import Article


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 특정 단일 게시글의 상세페이지를 응답(+단일 게시글 조회)
def detail(request, pk):
    # pk로 들어온 정수 값을 활용해 db에 id가 pk인 게시글을 조회 요청
    article = Article.objects.get(pk=pk)
    print(article)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html',context)    

# 게시글을 작성하기 위한 페이지를 제공하는 함수
def new(request):
    return render(request,'articles/new.html')

# 사용자로부터 데이터를 받아 저장하고 저장이 완료 되었다는 페이지를 제공하는 함수
def create(request):
    # 사용자로부터 받은 데이터 추출
    # print(request.GET)  # <QueryDict: {'title': ['ssafy'], 'content': ['python']}>
    title = request.POST.get('title')
    content = request.POST.get('content')

    # db에 저장요청(3가지 방법)
    # 1. 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.
    article = Article(title =title, content = content)
    article.save()

    # 3. 
    # Article.objects.create(title=title, content = content)
    
    # return render(request,'articles/create.html')
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # db에 삭제 요청
    article.delete()
    return redirect('articles:index')

def edit(request,pk):
    #몇 번 게시글 정보를 보여줄 지 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request,pk):
    # 어떤 글을 수정하는지 먼저 조회
    article = Article.objects.get(pk=pk)

    # 사용자 입력 데이터를 기존 인스턴스 변수에 새로 갱신
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)