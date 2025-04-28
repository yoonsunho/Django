from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Genre, Album, Review
from rest_framework.decorators import api_view
from .serializers import ArtistDetailSerializer, GenreSerializer, AlbumSerializer, ReviewSerializer, AlbumCreateSerializer, AlbumDetailSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def album_list_create(request):
    if request.method == 'GET':
        albums = get_list_or_404(Album)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AlbumCreateSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def album_retrieve_update_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    
    if request.method == 'GET':
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AlbumDetailSerializer(album, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def review_list_create(request, pk):
    album = get_object_or_404(Album, pk=pk)
    
    if request.method == 'GET':
        reviews = get_list_or_404(Review, album=album)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = ReviewSerializer(request,data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
@api_view(['GET', 'PUT', 'DELETE'])
def review_retrieve_update_delete(request, pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET'])
def review_sort_by(request, pk):
    album = get_object_or_404(Album, pk=pk)
    reviews = get_list_or_404(Review, album=album)

    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

    

@api_view(['GET', 'PUT', 'DELETE'])
def artist_retrieve_update_delete(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)
    
    if request.method == 'GET':
        serializer = ArtistDetailSerializer(artist)
        return Response(serializer.data)

@api_view(['GET'])
def genre_album(request,genre_pk):

    genre = Genre.objects.get(pk = genre_pk)
    serializer = GenreSerializer(genre, many=True)
    return Response(serializer.data)
    