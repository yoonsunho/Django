from rest_framework import serializers
from .models import Artist, Genre, Album, Review

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


        

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    # genres = GenreSerializer(many=True, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id','title','artist',)

class ReviewSerializer(serializers.ModelSerializer):

    album = AlbumSerializer(read_only = True)

    class Meta:
        model = Review
        fields = '__all__'



class AlbumDetailSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)


    class Meta:
        model = Album
        fields = '__all__'

    def get_review_count(self,obj):
        return(obj.review_count)


class AlbumCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'




class ArtistDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artist
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)




