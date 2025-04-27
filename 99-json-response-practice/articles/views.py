from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)  # Article.objects.all()처럼 QuerySet이나 리스트)를 시리얼라이저에 전달할 경우, many=True 옵션이 반드시 필요
    return Response(serializer.data)
