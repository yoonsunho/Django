from rest_framework import serializers
from .models import Artist, Genre, Album, Review

class ArtistSerializer(serializers.ModelSerializer):


    class Meta:
        model = Artist
        fields = ('id','name','albums',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content','rating',)
        read_only_fields = ('album',)

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    # genres = GenreSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id','title','artist',)


class AlbumDetailSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = '__all__'

    def get_review_count(self,obj):
        return obj.review_count


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class ArtistDetailSerializer(serializers.ModelSerializer):

    class AlbumTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album
            fields = ('id','title',)

    albums = AlbumTitleSerializer(read_only = True,many=True)
    
    class Meta:
        model = Artist
        fields = ('id','name','albums')

    

