from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.album_list_create, name='album_list_create'),
    path('albums/<int:pk>/', views.album_retrieve_update_delete, name='album_retrieve_update_delete'),
    path('albums/<int:pk>/reviews/', views.review_list_create, name='review_list_create'),
    path('albums/<int:pk>/reviews/<int:review_pk>/', views.review_retrieve_update_delete, name='review_retrieve_update_delete'),
    path('albums/<int:pk>/reviews/<str:sort_by>/', views.review_sort_by, name='review_sort_by'),
    path('artists/<int:artist_pk>/', views.artist_retrieve_update_delete, name='artist_retrieve_update_delete'),
]
 