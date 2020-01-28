from django.db import models
from django.contrib.auth.admin import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='profile/',default='default.png')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Artist(models.Model):
    image = models.ImageField(
        upload_to='images/', blank=True, default='Avatar.jpg', null=True)
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
    genre = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title
