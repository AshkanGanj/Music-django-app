
from django.contrib import admin
from django.urls import path, include
from music.views import Song_player
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', Song_player, name='Home'),
                  path('music/', include('music.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
