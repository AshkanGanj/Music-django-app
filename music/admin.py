from django.contrib import admin
from .models import Song, Album, Artist,Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
