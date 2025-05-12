from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# 모델 정보를 수정하는 문항이 없습니다.
# 모델 정보는 수정이 불가하며 수정시 loaddata 에 문제가 발생할 수 있습니다.
# 모델 정보 수정시 0점 처리됩니다.

# 아티스트 모델
class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 장르 모델
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 앨범 모델
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='albums')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist.name}'

# 리뷰 모델
class Review(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be at least 1"),
            MaxValueValidator(5, message="Rating cannot exceed 5")
        ]
    ) # 1~5 점 척도
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.album.title} 리뷰'
