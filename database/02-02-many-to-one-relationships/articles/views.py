from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_safe, require_POST

from .forms import ArticleForm, CommentForm
from .models import Article, Comment

@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 특정 게시글에 작성된 모든 댓글 조회 (역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET','POST'])       # 만약 아니면 405 RESPONSE CODE(method not allowed)
def create(request):    
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            # article.user = 게시글 작성을 요청하는 유저 객체
            # 현재 유저가 누구인지 db에서 찾을 필요 x
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET','POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 수저을 요청 시도하는 사용자와 게시글의 작성자가 같은지 확인
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else: 
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

@login_required
@require_POST
def comments_create(request, article_pk):
    # 어떤 게시글에 작성되는 댓글이 알려면 게시글을 먼저 조회
    article = Article.objects.get(pk=article_pk)
    # CommentForm을 활용한 댓글 생성
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 외래키 데이터를 넣으려면 댓글 인스턴스가 필요한데...
        # 댓글 인스턴스는 save() 호출이 완료되어야 반환됨
        # commit 키워드를 False로 바꾸면
        # 댓글 인스턴스는 생성해주지만 실제 DB에 아직 저장 요청은 보내지 않고 대기
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_POST
# 게시글 pk를 가져오는 두번째 방법 (url에서 넘겨주기)
def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글이 삭제되는 것인지 조회
    comment = Comment.objects.get(pk=comment_pk)
    # 게시글 pk를 가져오는 첫번째 방법 (댓글 삭제 전에 게시글 번호 저장해두기)
    # article_id = comment.article.pk
    # 댓글 삭제
    if request.user == comment.user:
        comment.delete()
    # 첫번째 방법에 대한 return
    # return redirect('articles:detail', article_id)
    # 두번째 방법에 대한 return
    return redirect('articles:detail', article_pk)
