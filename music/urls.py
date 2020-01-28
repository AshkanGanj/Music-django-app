from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('Albums/', views.Albums, name='Albums'),
    path('Albums_songs/<name>/', views.Albums_songs, name='AlbumsSongs'),
    path('Artist/', views.Artists, name='Artist'),
    path('Artist_songs/<name>/', views.Artist_songs, name='ArtistSongs'),
    path('search/', views.Search, name='Search'),
    path('edit/', views.update_profile, name='Edit')

]
