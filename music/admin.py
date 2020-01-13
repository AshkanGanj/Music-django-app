from django.contrib import admin
from .models import Song, Album, Artist,UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
