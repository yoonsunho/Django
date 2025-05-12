from rest_framework import serializers
from .models import Artist, Genre, Album, Review

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class AlbumListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album
            fields = ('id', 'title',)
            
    albums = AlbumListSerializer(many=True)
    
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # class ReviewCreateSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         fields = '__all__'
    
    # albums = ReviewCreateSerializer(read_only=True)
    
    
    class Meta:
        model = Review
        fields = ('content', 'rating',)

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    # genres = GenreSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'title', 'artist',)
        #except_fields = ('genres', 'reviews')


class AlbumDetailSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)


    class Meta:
        model = Album
        fields = '__all__'


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class ArtistDetailSerializer(serializers.ModelSerializer):
    class AlbumsListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album
            fields = ('id', 'title',)
            
    albums = AlbumsListSerializer(many=True)
    
    class Meta:
        model = Artist
        fields = '__all__'


