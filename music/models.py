from django.db import models
from django.contrib.auth.admin import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Artist(models.Model):
    image = models.ImageField(upload_to='images/', blank=True,default='Avatar.jpg',null=True)
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.CharField(max_length=40)
    album_title = models.CharField(max_length=40)
    album_image = models.FileField(default='', upload_to='album_logo/')

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.FileField(upload_to='songs/')
    image = models.ImageField(upload_to='images/')
    song_title = models.CharField(max_length=40)
    is_favorite = models.BooleanField(default=False)
    genre = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title
