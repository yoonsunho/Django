from django.db import models

# Create your models here.

# 게시글이 저장 될 테이블을 설계하는 클래스
class Article(models.Model):        # 장고->db->models모듈의 Model클래스를 가져옴(상속받음)
    
    title = models.CharField(max_length=10)     # title:테이블의 각 필드,CharField:modelfield(데이터 유형,제약 조건 정의)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uodated_at = models.DateTimeField(auto_now=True)