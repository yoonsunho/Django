from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    '''
    M:N 관계 설정 시 그냥 복수형으로 이름짓는 것 보다, 지금 우리가 만드는 기능이 무엇인지 생각해보고
    명시적인 매니저 이름을 설정하는 것이 좋다.
    
    게시글 1번에 좋아요를 누른 모든 유저 조회
    (Article -> User/참조)
    
    '게시글1.users.all)' 표현을 다음과 같이 표현할 것이다
    '게시글1.like_users.all()'
    '''
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
