[TOC]

# Django Field Lookups

[QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups)

데이터베이스 쿼리를 작성할 때, 모델 필드에 대한 조건을 **직관적**이고 **유연**하게 표현할 수 있도록 해주는 기능
Django에서는 `__`(더블 언더스코어)를 통해 **필드명**과 **조회 조건(lookup type)**을 연결하여 `filter()`, `exclude()` 등으로 손쉽게 필터링 로직을 구성할 수 있음

```python
Article.objects.filter(title__startswith="Django")
```

> `title` 필드가 `"Django"`로 시작하는 `Article` 데이터(레코드)를 찾아준다는 의미

------

## 1. 기본 예시 모델

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```



---



## 2. 주요 Field Lookups 예시

### 2.1 exact / iexact

- **exact**: 대소문자를 **구분**하여 정확히 일치하는 값을 찾음
- **iexact**: 대소문자 구분 없이(대소문자 무시) 정확히 일치하는 값을 찾음

```python
# title이 "Django"와 정확히 일치하는 기사
articles_exact = Article.objects.filter(title__exact="Django")

# 대소문자 구분 없이 "django"와 일치하는 기사
articles_iexact = Article.objects.filter(title__iexact="django")
```

### 2.2 contains / icontains

- **contains**: 문자열 내에 특정 값이 **포함**되어 있는지 (대소문자 구분)
- **icontains**: 문자열 포함 여부를 대소문자 구분 없이 확인

```python
# content에 "ORM"이 포함된 기사
articles_contains = Article.objects.filter(content__contains="ORM")

# content에 "orm"이 포함된 기사(대소문자 구분 X)
articles_icontains = Article.objects.filter(content__icontains="orm")
```

### 2.3 startswith / istartswith, endswith / iendswith

- **startswith / istartswith**: 필드의 값이 특정 문자열로 **시작**하는지 체크
- **endswith / iendswith**: 필드의 값이 특정 문자열로 **끝**나는지 체크

```python
# 제목이 'D'로 시작하는 기사
articles_startswith = Article.objects.filter(title__startswith="D")

# 제목이 'logy'로 끝나는 기사 (대소문자 구분 없이)
articles_iendswith = Article.objects.filter(title__iendswith="logy")
```

### 2.4 비교 연산자 (gt, gte, lt, lte)

- 숫자 또는 날짜 필드에 대해 **크거나 작음**을 비교

```python
from datetime import datetime

# created_at이 2025년 1월 1일 이후인 기사
articles_after_date = Article.objects.filter(created_at__gt=datetime(2025, 1, 1))
```

- **gt**: `>` (보다 큼)
- **gte**: `>=`
- **lt**: `<`
- **lte**: `<=`

### 2.5 in

- 여러 값 중 하나와 일치할 때 조회

```python
# title이 "Django" 또는 "Python"인 기사
articles_in = Article.objects.filter(title__in=["Django", "Python"])
```

### 2.6 range

- 범위 내에 있는 값을 조회 (숫자·날짜 모두 가능)

```python
# created_at이 2023-01-01 ~ 2025-12-31 사이인 기사
articles_in_range = Article.objects.filter(
    created_at__range=["2023-01-01", "2025-12-31"]
)
```

### 2.7 isnull

- 필드 값이 `NULL`인지 확인

```python
# content 필드가 NULL인 기사
articles_isnull = Article.objects.filter(content__isnull=True)
```



---



## 3. 정리

- **직관적인 문법**: `filter()`, `exclude()` 등에 `__` 문법을 적용하면, SQL 없이도 **복잡한 쿼리를 쉽게** 작성할 수 있음
- **다양한 조건**: 문자열 검색, 비교 연산, 범위 검색, NULL 검사 등 **광범위한 조회 조건**을 지원
- **가독성 향상**: “어떤 필드를 어떤 조건으로 필터링하는지”가 코드 레벨에서 명확히 드러나므로, 유지보수와 디버깅이 수월

**Django Field Lookups**을 잘 활용하면, `DB 조회 로직`을 **간결하고 효율적**으로 작성할 수 있음