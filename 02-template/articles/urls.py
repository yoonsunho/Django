from django.urls import path
# 명시적 상대경로
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail),
    
]