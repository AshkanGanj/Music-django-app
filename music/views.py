from django.shortcuts import render, redirect
from .models import Song, Album, Artist, Profile
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import ProfileForm, UserForm
from django.db import transaction
from django.contrib import messages


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form = user_form.save()
            profile_form = profile_form.save()
            return redirect('Home')
        else:
            return redirect('Edit')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': ProfileForm
    }
    return render(request, 'create.html', context)


def Search(request):
    songs = Song.objects
    query = request.GET.get("search")
    if query is not None:
        songs = songs.filter(song__icontains=query)
        if songs:
            return render(request, 'Home.html', {'songs': songs})
        elif songs:
            songs = songs.filter(artist__name__icontains=query)
            return render(request, 'Home.html', {'songs': songs})
        elif songs:
            songs = songs.filter(album__album_title=query)
            return render(request, 'Home.html', {'songs': songs})
        else:
            messages.error(request,"entered info not valid !")
            return redirect('Home')
    else:
        return redirect('Home')


def SignUp(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            try:
                User.objects.get(username=request.POST["sign_username"])
                return render(request, 'SignUp.html', {'error': 'Username  has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST["sign_username"], password=request.POST["password1"])
                return redirect('Home')
        else:
            return render(request, 'SignUp.html', {'error': 'Password does not match'})
    else:
        return render(request, 'SignUp.html')


def Login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['Login_username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('Home')
        else:
            return render(request, 'Login.html', {'error': 'Password or username  not match'})
    return render(request, 'Login.html')


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('Home')
    return render(request, 'Home.html')


def Albums(request):
    albums = Album.objects
    return render(request, 'Albums.html', {'Albums': albums})


def Albums_songs(request, name):
    musics = Song.objects.filter(album__album_title=name)
    return render(request, 'Albums_songs.html', {'Musics': musics})


def Song_player(request):
    songs = Song.objects
    artists = Artist.objects
    return render(request, 'Home.html', {'songs': songs})


def Artists(request):
    artists = Artist.objects
    return render(request, 'Artist.html', {'Artists': artists})


def Artist_songs(request, name):
    artist = Song.objects.filter(artist__name=name)
    return render(request, 'Artist_songs.html', {'Artist': artist})


@login_required
def AddToPlayList(request):
    pass
